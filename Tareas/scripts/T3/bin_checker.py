import json
import numpy as np

def check_output(testfile, student_output, jsonfile):
    try:
        tests = ["easy_0", "easy_1", "easy_2", "easy_3",
            "medium_0", "medium_1", "medium_2", "medium_3",
            "hard_0", "hard_1", "hard_2", "hard_3"]
        for test in tests:
            if test in testfile:
                key = test
                break
        with open(testfile, "r") as test:
            check = [int(i) for i in test.readlines()]
            capacidad = check[0]
            cant_item = check[1]
            items = np.array(check[2:])
            sum_items = sum(items)
        with open(student_output, "r") as out:
            output = out.readlines()
            objetivo = int(output[0])

            if len(output[1:]) != objetivo:
                return "WRONG OUTPUT", 0    

            cant_items_al = 0
            sum_tot = 0
            for knapsack in output[1:]:
                items_al = list(map(int, knapsack.split()))
                cant_items_al += len(items_al)
                if sum(items[items_al]) > capacidad:
                    return "WRONG OUTPUT", 0
                sum_tot += sum(items[items_al])
            if cant_items_al != cant_item:
                return "WRONG OUTPUT", 0

            if sum_items != sum_tot:
                return "WRONG OUTPUT", 0

        with open(jsonfile, "r") as file:
            optimos = json.load(file)

            if objetivo/optimos[key] > 1.30:
                return "WRONG OUTPUT", 0
            elif objetivo/optimos[key] > 1.20:
                return "PARTIAL CORRECT", 0.5
            elif objetivo/optimos[key] > 1:
                return "PARTIAL CORRECT", 0.67
            else:
                return "CORRECT", 1
    except FileNotFoundError:
        return "WRONG PATH", 0
    except Exception:
        return "WRONG OUTPUT FORMAT", 0

if __name__ == '__main__':
    # PUEDES REESCRIBIR ESTA SECCION PARA AUTOMATIZAR TU REVISION
    test_file_path = input("Introduce el path del archivo de test: ")
    output_file_path = input("Introduce el path de tu archivo de output: ")
    jsonfile = input("Introduce el path del archivo de pauta: ")

    score = check_output(test_file_path, output_file_path, jsonfile)
    print('Score: {}'.format(score))

