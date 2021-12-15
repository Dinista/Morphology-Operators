import numpy as np
import os
import sys 
import cv2
from os import walk
from skimage.filters.rank import maximum, minimum
from skimage.morphology import reconstruction
from skimage.segmentation import join_segmentations

# Le as imagens presentes no diretorio raiz, e carrega a escolhida.
# Após isso seleciona o operador a ser utilizado.

def select_img():
    print("===========================================")
    print("Digite o número correspondente a imagem que deseja carregar:\n")
    filenames = next(walk(os.path.dirname(__file__) + "/"), (None, None, []))[2]
    files = [ file for file in filenames if file.endswith((".jpg", ".JPG", ".PNG", ".png", ".tif", ".tiff", ".TIF")) ]
    
    if len(files) == 0:
        print("Não existe arquivos de imagem no diretório raiz.")
        sys.exit()
    
    for i in range(0, len(files)):
        print('[{}] {}'.format(i, files[i]))
    index = input()
    
    while not index.isdigit() or int(index) >= len(files) or int(index) < 0:
        print("\nEsta opção não existe, digite novamente.")
        index = input()
    
    imagem = cv2.imread(os.path.dirname(__file__) + "/" + files[int(index)], cv2.IMREAD_GRAYSCALE)
    
    print("\nSelecione o operador que deseja utilizar:")
    print("\n[1] Fechamento de buracos.")
    print("[2] Limpeza de borda.")
    operator = input()    

    while(not operator.isdigit() or (int(operator) != 2 and int(operator) != 1)):
        print("\nValor inválido! Digite novamente:")
        operator = input()

    return imagem, int(operator), files[int(index)]
    

# Aplica o preenchimento de buracos

def filling_holes(image):
    seed = np.copy(image)
    seed[1:-1, 1:-1] = image.max()
    mask = image
    filled = reconstruction(seed, mask, method='erosion')
    return filled


# Aplica a limpeza de borda

def border_clearing(image):
    seed = np.copy(image)
    seed[1:-1, 1:-1] = image.min()
    mask = image
    filled = reconstruction(seed, mask, method='dilation')
    result = image - filled
    return result


def main():
    imagem, operator, nome_arq = select_img()
    
    if operator == 1:
        img_result = filling_holes(imagem)
        msg = "Imagem preenchida"
        msg_save = "preechida"
        name_save = "buracos"
    else:
        img_result = border_clearing(imagem)
        msg = "Imagem com bordas limpas"
        msg_save = "sem bordas"
        name_save = "bordas"
    
    print("\nFeche as janelas para continuar...")
    cv2.imshow('Imagem binaria', imagem)
    cv2.imshow(msg, img_result)
    cv2.waitKey(0)
    print("\nGostaria de salvar a imagem " + msg_save + "?\n[1] Sim\n[2] Não")
    op = input()
    while op != '1' or op != '2':
        if op == '2' or op == '1': break
        print("\nEsta opção não existe, tente novamente.")
        op = input()
    
    #salvando a imagem

    if op == '1':
        aux = nome_arq.split(".")
        cv2.imwrite(os.path.dirname(__file__) + "/" + str(name_save) +"_"+ aux[0] +'.jpg', img_result)
        print("\nSalvo em:\n" + os.path.dirname(__file__))
    
    print("\nPrograma encerrado.")
if __name__ == "__main__":
    main()
