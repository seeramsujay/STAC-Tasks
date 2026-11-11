import subprocess
from pathlib import Path

def test_euler_prob1():
    src = Path("software/Task-04/Euler-Prob1.c")
    assert src.exists()
    bin_path = Path("/tmp/euler1_test")
    compile_res = subprocess.run(["gcc", str(src), "-o", str(bin_path)], capture_output=True, text=True)
    assert compile_res.returncode == 0, compile_res.stderr
    run_res = subprocess.run([str(bin_path)], capture_output=True, text=True)
    assert run_res.returncode == 0
    assert run_res.stdout.strip() == "233168"
    bin_path.unlink(missing_ok=True)

def test_euler_prob2():
    src = Path("software/Task-04/Euler-Prob2.c")
    assert src.exists()
    bin_path = Path("/tmp/euler2_test")
    compile_res = subprocess.run(["gcc", str(src), "-o", str(bin_path)], capture_output=True, text=True)
    assert compile_res.returncode == 0, compile_res.stderr
    run_res = subprocess.run([str(bin_path)], capture_output=True, text=True)
    assert run_res.returncode == 0
    assert run_res.stdout.strip() == "4613732"
    bin_path.unlink(missing_ok=True)

def test_segr_script():
    sh_file = Path("software/Task-01/segrV2.sh")
    assert sh_file.exists()
    assert len(sh_file.read_text()) > 0
