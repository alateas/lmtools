def main():
    from dhcp import Dhcp
    from network import Ip
    import test_pass

    dhcp = Dhcp(test_pass.info['server'], test_pass.info['login'], test_pass.info['password'])
    print dhcp.create_lease_in_range(Ip(192,168,107,17), Ip(192,168,107,30), 'asd')

if __name__ == '__main__':
    main()