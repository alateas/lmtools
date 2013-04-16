def main():
    from dhcp import Dhcp
    from network import Ip
    import test_pass

    dhcp = Dhcp(test_pass.info['server'], test_pass.info['login'], test_pass.info['password'])
    print dhcp.get_range(Ip(192,168,107,0), Ip(192,168,107,10))

if __name__ == '__main__':
    main()