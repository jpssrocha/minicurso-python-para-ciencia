from astropy.io import fits

def combinar_imagens(lista_de_arquivos, nome_da_saida):
    """
    Dada uma lista de arquivos FITS, combina as imagens
    e escreve o resultado em disco
    
    Entrada:
        lista_de_arquivos: lista ou coleção de string
            Nomes dos arquivos para combinar
        nome_da_saida: string
            Nome para gravar arquivo
            
    Transformações de arquivo:
        Grava novo arquivo FITS, com nome passado em nome_da_saida
        
    Retorno:
        imagem_final: array 2D do NumPy
            Imagem combinada
        hdr: astropy.io.fits.header.Header
            Cabeçalho da primeira imagem
    """
    # Carregando imagens
    imagens = [fits.getdata(arquivo) for arquivo in arquivos_bias]
    hdr = fits.getheader(lista_de_arquivos[0])
    imagem1 = imagens[0]
    
    # Fazendo combinação
    image_cube = np.stack(imagens, axis=0)
    final_image = np.median(image_cube, axis=0)
    
    print(f"sigma inicial:  {np.std(imagem1)} \t sigma final: {np.std(final_image)}")
    
    # Escrevendo resultado no disco
    fits.writeto(nome_da_saida, final_image, hdr)
    
    return final_image, hdr