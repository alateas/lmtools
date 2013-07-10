def main():
    from dhcp import Dhcp
    from network import Ip, Mac
    import test_pass
    import logger

    dhcp = Dhcp(test_pass.info['server'], test_pass.info['login'], test_pass.info['password'])
    # print dhcp.get_range(Ip(192,168,107,4), Ip(192,168,107,10))
    # logger.log('test1', 'asds')

if __name__ == '__main__':
    main()