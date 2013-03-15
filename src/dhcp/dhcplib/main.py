def main():
    from dhcp import Dhcp
    dhcp = Dhcp()
    print dhcp.get_range(110)

if __name__ == '__main__':
    main()