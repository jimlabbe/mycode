from netmiko import ConnectHandler
'''This code logs into a remote computer, passes to it configurations, and then closes the connection'''

def bootstrapper(dev_type, dev_ip, dev_un, dev_pw, config):
    try:
        with open(config, 'r')  as config_file:
            config_lines = config_file.read().splitlines()
            #open up the config file and chop it up into csv-friendly format
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        open_connection.enable() #grants admin -level power for anycommands
        
        # pass config to the send_config_set() method
        output = open_connection.send_config_set(config_lines)
        print(output)
        open_connection.send_command_expect('write memory') #save the changes and commit
        open_connection.disconnect()

        return True
    except Exception as err:
        print(err)
        return False

