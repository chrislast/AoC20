import sys
import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22
import day23
import day24
import day25
from utils import FAILED, PASSED, RAN, SKIPPED
t=lambda n:{1:"test "}.get(n,"tests")
print(f"""
{SKIPPED:-3d} {t(SKIPPED)} skipped
{RAN:-3d} {t(RAN)} executed
{PASSED:-3d} {t(PASSED)} passed
{FAILED:-3d} {t(FAILED)} failed
""")
sys.exit(FAILED)
