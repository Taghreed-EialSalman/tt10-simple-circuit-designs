import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

def pack_abc(a, b, c):
    # A->bit0, B->bit1, C->bit2
    return ((c & 1) << 2) | ((b & 1) << 1) | (a & 1)

def get_bit(val, bit):
    return (val >> bit) & 1

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 10, unit="us")  # (fix deprecation warning)
    cocotb.start_soon(clock.start())

    dut._log.info("Reset")
    if hasattr(dut, "ena"):
        dut.ena.value = 1

    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    tests = [
        (0, 0, 0, 1),  # expected F
        (0, 0, 1, 0),
        (0, 1, 0, 1),
    ]

    for (a, b, c, exp_f) in tests:
        dut.ui_in.value = pack_abc(a, b, c)
        await ClockCycles(dut.clk, 25)

        out = int(dut.uo_out.value)
        f0 = get_bit(out, 0)

        dut._log.info(f"A={a} B={b} C={c}  ui_in={int(dut.ui_in.value):#04x}  uo_out={out:#04x}  F(bit0)={f0}")

        assert f0 == exp_f, f"Expected F={exp_f} for A={a},B={b},C={c} but got uo_out={out:#04x}"
