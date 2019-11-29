try:
    a=int(input())
except EOFError:
    print("EOFError")
except ValueError:
    print("ValueError")
except KeyboardInterrupt:
    print("KeyboardInterrupt")