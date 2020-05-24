"""
States with counts for reporting
"""

class StateCount:

    def __init__(self, threshold):
        self.count: int = 0
        self.error: int = 0
        self.fails: int = 0
        self.skip: int = 0
        self.warn: int = 0
        self.passes: int = 0
        self.threshold: float = threshold

    def update(self, error: bool, fails: bool, skip: bool, warn: bool):
        self.count += 1

        if error:
            self.error += 1
        if fails:
            self.fails += 1
        if skip:
            self.skip += 1
        if warn:
            self.warn += 1

        if not (error or fails):
            self.passes += 1
