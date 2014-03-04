__author__ = 'Administrator'
"""
贪婪算法（greedy method）：采用逐步构造最优解的方法。
在每个阶段，都作出一个看上去最优的决策（在一定的标准下）。
决策一旦作出，就不可再更改。作出贪婪决策的依据称为贪婪准则（greedy criterion）。 

贪婪算法的关键：
1）每步贪婪；
2）不回溯；
3）选择的规则(criterion)非常重要，
不正确的规则可能得不到结果、
不优化或者不能作为贪婪的求解对象；
4）必定有解，但是可能不会得到最优解。
"""
results = {
#    'TEST': (  TIME, set([COVERED_POINT ...])),
  'test_00': (  2.08, set([2, 3, 5, 11, 12, 16, 19, 23, 25, 26, 29, 36, 38, 40])),
  'test_01': ( 58.04, set([0, 10, 13, 15, 17, 19, 20, 22, 27, 30, 31, 33, 34])),
  'test_02': ( 34.82, set([3, 4, 6, 12, 15, 21, 23, 25, 26, 33, 34, 40])),
  'test_03': ( 32.74, set([4, 5, 10, 16, 21, 22, 26, 39])),
  'test_04': (100.00, set([0, 1, 4, 6, 7, 8, 9, 11, 12, 18, 26, 27, 31, 36])),
  'test_05': (  4.46, set([1, 2, 6, 11, 14, 16, 17, 21, 22, 23, 30, 31])),
  'test_06': ( 69.57, set([10, 11, 15, 17, 19, 22, 26, 27, 30, 32, 38])),
  'test_07': ( 85.71, set([0, 2, 4, 5, 9, 10, 14, 17, 24, 34, 36, 39])),
  'test_08': (  5.73, set([0, 3, 8, 9, 13, 19, 23, 25, 28, 36, 38])),
  'test_09': ( 15.55, set([7, 15, 17, 25, 26, 30, 31, 33, 36, 38, 39])),
  'test_10': ( 12.05, set([0, 4, 13, 14, 15, 24, 31, 35, 39])),
  'test_11': ( 52.23, set([0, 3, 6, 10, 11, 13, 23, 34, 40])),
  'test_12': ( 26.79, set([0, 1, 4, 5, 7, 8, 10, 12, 13, 31, 32, 40])),
  'test_13': ( 16.07, set([2, 6, 9, 11, 13, 15, 17, 18, 34])),
  'test_14': ( 40.62, set([1, 2, 8, 15, 16, 19, 22, 26, 29, 31, 33, 34, 38])),
 }
'''
贪婪排名算法的核心是对当前选择测试的子集进行排序：
至少用一个测试集覆盖尽可能大的范围。
经过第一个步骤，逐步减少测试集，同时覆盖尽可能大的范围。
给选择的测试做出一个排序，这样小数据集的测试也可以选择使用
完成上述排序后，接下来就可以优化算法的执行时间了
当然，他需要能在很大的测试集下工作。
贪婪排名算法的工作原理就是先选择当前测试集的某一项的最优解，然后寻找下一项的最优解，依次进行...
如果有两个以上的算法得出相同的执行结果，那么将以执行”时间“来比较两种算法优劣。'''

def greedyranker(results):
    results = results.copy()
    ranked, coveredsofar, costsofar, round = [], set(), 0, 0
    noncontributing = []
    while results:
        round += 1
        # What each test can contribute to the pool of what is covered so far
        contributions = [(len(cover - coveredsofar), -cost, test)
                         for test, (cost, cover) in sorted(results.items()) ]
        # Greedy ranking by taking the next greatest contributor
        delta_cover, benefit, test = max( contributions )
        if delta_cover > 0:
            ranked.append((test, delta_cover))
            cost, cover = results.pop(test)
            coveredsofar.update(cover)
            costsofar += cost
        for delta_cover, benefit, test in contributions:
            if delta_cover == 0:
                # this test cannot contribute anything
                noncontributing.append( (test, round) )
                results.pop(test)
    return coveredsofar, ranked, costsofar, noncontributing

def greedyranker2(results, tutor=True):
    results = results.copy()
    ranked, coveredsofar, costsofar, round = [], set(), 0, 0
    noncontributing = []
    while results:
        round += 1
        # What each test can contribute to the pool of what is covered so far
        contributions = [(len(cover - coveredsofar), -cost, test)
                         for test, (cost, cover) in sorted(results.items()) ]
        if tutor:
            print('\n## Round %i' % round)
            print('  Covered so far: %2i points: ' % len(coveredsofar))
            print('  Ranked so far: ' + repr([t for t, d in ranked]))
            print('  What the remaining tests can contribute, largest contributors first:')
            print('    # DELTA, BENEFIT, TEST')
            deltas = sorted(contributions, reverse=True)
            for delta_cover, benefit, test in deltas:
                print('     %2i,    %7.2f,    %s' % (delta_cover, benefit, test))
            if len(deltas)>=2 and deltas[0][0] == deltas[1][0]:
                print('  Note: This time around, more than one test gives the same')
                print('        maximum delta contribution of %i to the coverage so far'
                       % deltas[0][0])
                if deltas[0][1] != deltas[1][1]:
                    print('        we order based on the next field of minimum cost')
                    print('        (equivalent to maximum negative cost).')
                else:
                    print('        the next field of minimum cost is the same so')
                    print('        we arbitrarily order by test name.')
            zeroes = [test for delta_cover, benefit, test in deltas
                     if delta_cover == 0]
            if zeroes:
                print('  The following test(s) cannot contribute more to coverage')
                print('  and will be dropped:')
                print('    ' + ', '.join(zeroes))

        # Greedy ranking by taking the next greatest contributor
        delta_cover, benefit, test = max( contributions )
        if delta_cover > 0:
            ranked.append((test, delta_cover))
            cost, cover = results.pop(test)
            if tutor:
                print('  Ranking %s in round %2i giving extra coverage of: %r'
                       % (test, round, sorted(cover - coveredsofar)))
            coveredsofar.update(cover)
            costsofar += cost

        for delta_cover, benefit, test in contributions:
            if delta_cover == 0:
                # this test cannot contribute anything
                noncontributing.append( (test, round) )
                results.pop(test)
    if tutor:
        print('\n## ALL TESTS NOW RANKED OR DISCARDED\n')
    return coveredsofar, ranked, costsofar, noncontributing

totalcoverage, ranking, totalcost, nonranked = greedyranker(results)
print('''
A total of %i points were covered,
using only %i of the initial %i tests,
and should take %g time units to run.

The tests in order of coverage added:

    TEST  DELTA-COVERAGE'''
 % (len(totalcoverage), len(ranking), len(results), totalcost))
print('\n'.join('  %6s  %i' % r for r in ranking))
