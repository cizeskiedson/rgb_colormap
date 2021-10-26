import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import sys
import getopt

def help():
    print("\nErro na leitura dos parametros\n")
    print("Digite python3 trab.py -i nome_da_imagem -p nome_da_paleta\n")
    print("Paletas disponiveis: \n")
    print(plt.colormaps())
    print("\nImagens disponiveis: \n")
    print(os.listdir(dirImagens()))
    print("================================\n")

def dirImagens():
    dir_atual = os.path.dirname(os.path.realpath('__file__'))
    return os.path.join(dir_atual, 'fotos/')

def leArquivo():
    """Funcao que le os parametros e a foto.
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:p:h', ['imagem=', 'paleta=', 'help'])
    except getopt.GetoptError:
        help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit(2)
        elif opt in ('-i', '--imagem'):
            imagem = arg
        elif opt in ('-p', '--paleta'):
            paleta = arg
            if paleta not in plt.colormaps():
                help()
                sys.exit(2)
        else:
            sys.exit(2)
    nome_img = os.path.join(dirImagens(), imagem)
    img = cv2.imread(nome_img, cv2.IMREAD_GRAYSCALE)
    return img, paleta

def aplicaPaleta(img_cinza, paleta):

    paleta = paleta(np.arange(0, 256)) * 255

    paleta_r = paleta[::, 2]
    paleta_g = paleta[::, 1]
    paleta_b = paleta[::, 0]

    canais = (np.uint8(paleta_r[img_cinza]), 
                np.uint8(paleta_g[img_cinza]), 
                np.uint8(paleta_b[img_cinza]))

    return np.dstack(canais)

def main():
    """Fluxo principal.
    """
    img, paleta = leArquivo()
    paleta = plt.get_cmap(paleta)
    img_plt = aplicaPaleta(img, paleta)
    cv2.imshow('image', img_plt)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()