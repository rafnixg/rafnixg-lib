"""RafnixG - Personal Card"""
from rafnixg import RafnixG


def main():
    """Main function."""
    me = RafnixG()
    me.get_links()
    me.posts()
    me.display()

if __name__ == '__main__':
    main()
