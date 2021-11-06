from bootstrap_yield_curve import BootstrapYieldCurve
import matplotlib.pyplot as plt

yield_curve = BootstrapYieldCurve()
yield_curve.add_instrument(100, 0.25, 0., 97.5)
yield_curve.add_instrument(100, 0.5, 0., 94.9)
yield_curve.add_instrument(100, 1.0, 0., 90.)
yield_curve.add_instrument(100, 1.5, 8, 96., 2)
yield_curve.add_instrument(100, 2., 12, 101.6, 2)
y = yield_curve.get_zero_rates()
x = yield_curve.get_maturities()

xy = yield_curve.get_maturities_zero_rates()

print(sorted(x))
print(y)

# plt.plot(x, y)
plt.plot(xy.keys(), xy.values())
plt.title("Zero Curve")
plt.ylabel("Zero Rate (%)")
plt.xlabel("Maturity in Years")
plt.show()