def argv():
    import argparse

    parser = argparse.ArgumentParser(description=f'Example command:\
    --mode=server')
    parser.add_argument("--startOpt", default='desktop', type=str,
                        help="operating mode desktop or server")
    args = parser.parse_args()
    startOpt = args.startOpt
    return startOpt
