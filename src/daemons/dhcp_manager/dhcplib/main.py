def main():
    from dhcp import Dhcp
    import test_pass

    dhcp = Dhcp(test_pass.info['server'], test_pass.info['login'], test_pass.info['password'])
    print dhcp.get_range(110)

if __name__ == '__main__':
    main()