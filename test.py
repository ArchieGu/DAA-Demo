from Path.Map.utils import gen_random_province

def test_gen_random_province():
    prov = gen_random_province()
    print(prov)
    assert prov != ""

if __name__ == '__main__':
    test_gen_random_province()