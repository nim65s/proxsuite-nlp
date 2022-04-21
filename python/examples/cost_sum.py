import proxnlp
import numpy as np

from proxnlp import manifolds
from proxnlp.costs import CostSum, QuadraticDistanceCost


space = manifolds.SE2()
p0 = space.neutral()
p1 = space.rand()
p2 = space.rand()
print("p0:", p0)
print("p1:", p1)
print("p2:", p2)

weights = np.eye(space.ndx)

dist_fun0 = QuadraticDistanceCost(space, p0, weights)
dist_fun1 = QuadraticDistanceCost(space, p1, weights)
dist_fun2 = QuadraticDistanceCost(space, p2, weights)

Hg0 = dist_fun0.computeHessian(p0)
Hg1 = dist_fun1.computeHessian(p0)
print("Hg0\n{}".format(Hg0))
print("Hg1\n{}".format(Hg1))

print("scalar * CostFunction:      ", 0.5 * dist_fun1)
print("CostFunction + CostFunction:", dist_fun0 + dist_fun1)

def test_cost_sum():
    sum_1 = CostSum(space.nx, space.ndx)
    print("sum1 init:", sum_1)
    sum_1.add_component(dist_fun0)
    print("add_comp :", sum_1)
    sum_1 += dist_fun1
    print("after += :", sum_1)
    sum_1 *= 0.5
    print("after *= :", sum_1)
    print("sum1.weights:", sum_1.weights.tolist())
    Hs_1 = sum_1.computeHessian(p0)
    print("Hessian of sum_1\n{}".format(Hs_1))

    assert np.allclose(Hs_1, .5 * (Hg0 + Hg1)), "Should be\n{}".format(0.5 * (Hg0 + Hg1))

    sum_2 = dist_fun0 + dist_fun1
    print("sum2 init:", sum_2)
    sum_2 *= 0.5
    print("after *= :", sum_2)
    Hs_2 = sum_2.computeHessian(p0)
    assert np.allclose(Hs_2, .5 * (Hg0 + Hg1)), "Should be\n{}".format(0.5 * (Hg0 + Hg1))

    sum_3 = sum_2 + 0.5 * dist_fun2
    print("sum3 init:", sum_3)
    prob = proxnlp.Problem(sum_2)
    ws = proxnlp.Workspace(space.nx, space.ndx, prob)
    rs = proxnlp.Results(space.nx, prob)
    solver = proxnlp.Solver(space, prob, mu_init=0.1)
    flag = solver.solve(ws, rs, p0, [])
    print("Flag:", flag)
    print("xopt:", rs.xopt)


if __name__ == '__main__':
    test_cost_sum()