def test000():
    """
    Hack to get nose to run tests properly.
    This file should be the first file processed by a nosetests run.
    """

    # Add parent directory to system path
    # as per answer http://stackoverflow.com/a/1054293
    # to question http://stackoverflow.com/q/1054271 .
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), 
                os.path.pardir,
                )
            )
        )
test000()
