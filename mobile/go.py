import os
import requests

def criar_pastas():
    pastas = [
        "videos/horizontal", 
        "videos/vertical",
        "fotos/vertical", 
        "fotos/horizontal", 
        "fotos/square"
    ]
    for pasta in pastas:
        os.makedirs(pasta, exist_ok=True)

def baixar_arquivo(url, caminho_destino):
    if os.path.exists(caminho_destino):
        print(f"Já existe: {caminho_destino} — pulando download.")
        return
    try:
        print(f"Baixando: {caminho_destino}")
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(caminho_destino, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")

downloads = [
    # Exemplo de entradas — adicione o restante aqui
    ("https://videos.pexels.com/video-files/4087103/4087103-uhd_2560_1440_25fps.mp4", "videos/horizontal/01.mp4"),
    ("https://videos.pexels.com/video-files/3141320/3141320-uhd_2560_1440_25fps.mp4", "videos/horizontal/02.mp4"),
    ("https://videos.pexels.com/video-files/7326212/7326212-hd_1920_1080_24fps.mp4", "videos/horizontal/03.mp4"),
    ("https://videos.pexels.com/video-files/6337126/6337126-uhd_2560_1440_25fps.mp4", "videos/horizontal/04.mp4"),
    ("https://videos.pexels.com/video-files/6963971/6963971-hd_1920_1080_25fps.mp4", "videos/horizontal/05.mp4"),
    ("https://videos.pexels.com/video-files/4904253/4904253-uhd_2560_1440_24fps.mp4", "videos/horizontal/06.mp4"),
    ("https://videos.pexels.com/video-files/8428489/8428489-uhd_2732_1440_25fps.mp4", "videos/horizontal/07.mp4"),
    ("https://videos.pexels.com/video-files/5199842/5199842-uhd_2560_1440_25fps.mp4", "videos/horizontal/08.mp4"),
    ("https://videos.pexels.com/video-files/8444033/8444033-uhd_2732_1440_25fps.mp4", "videos/horizontal/09.mp4"),
    ("https://videos.pexels.com/video-files/3044154/3044154-uhd_2560_1440_25fps.mp4", "videos/horizontal/10.mp4"),
    ("https://videos.pexels.com/video-files/18744336/18744336-hd_1080_1920_24fps.mp4", "videos/vertical/01.mp4"),
    ("https://videos.pexels.com/video-files/30850852/13193215_1440_2560_30fps.mp4", "videos/vertical/02.mp4"),
    ("https://videos.pexels.com/video-files/27633462/12189355_1080_1920_25fps.mp4", "videos/vertical/03.mp4"),
    ("https://videos.pexels.com/video-files/8104552/8104552-hd_1080_1774_30fps.mp4", "videos/vertical/04.mp4"),
    ("https://videos.pexels.com/video-files/6466345/6466345-uhd_1440_2732_25fps.mp4", "videos/vertical/05.mp4"),
    ("https://videos.pexels.com/video-files/8381147/8381147-uhd_1440_2560_25fps.mp4", "videos/vertical/06.mp4"),
    ("https://videos.pexels.com/video-files/30108415/12913969_1080_1920_25fps.mp4", "videos/vertical/07.mp4"),
    ("https://videos.pexels.com/video-files/7525494/7525494-hd_1080_1920_25fps.mp4", "videos/vertical/08.mp4"),
    ("https://videos.pexels.com/video-files/19784279/19784279-uhd_1440_2560_60fps.mp4", "videos/vertical/09.mp4"),
    ("https://videos.pexels.com/video-files/6202079/6202079-uhd_1440_2560_24fps.mp4", "videos/vertical/10.mp4"),
    ("https://images.pexels.com/photos/3892469/pexels-photo-3892469.jpeg", "fotos/square/01.jpg"),
    ("https://images.pexels.com/photos/3892468/pexels-photo-3892468.jpeg", "fotos/square/02.jpg"),
    ("https://images.pexels.com/photos/18205769/pexels-photo-18205769.jpeg", "fotos/square/03.jpg"),
    ("https://images.pexels.com/photos/8696529/pexels-photo-8696529.jpeg", "fotos/square/04.jpg"),
    ("https://images.pexels.com/photos/25819944/pexels-photo-25819944.jpeg", "fotos/square/05.jpg"),
    ("https://images.pexels.com/photos/15823267/pexels-photo-15823267.jpeg", "fotos/square/06.jpg"),
    ("https://images.pexels.com/photos/20212456/pexels-photo-20212456.jpeg", "fotos/square/07.jpg"),
    ("https://images.pexels.com/photos/4451666/pexels-photo-4451666.jpeg", "fotos/square/08.jpg"),
    ("https://images.pexels.com/photos/2074118/pexels-photo-2074118.jpeg", "fotos/square/09.jpg"),
    ("https://images.pexels.com/photos/10026524/pexels-photo-10026524.png", "fotos/square/10.jpg"),
    ("https://images.pexels.com/photos/5749105/pexels-photo-5749105.jpeg", "fotos/horizontal/01.jpg"),
    ("https://images.pexels.com/photos/32713518/pexels-photo-32713518.jpeg", "fotos/horizontal/02.jpg"),
    ("https://images.pexels.com/photos/11079279/pexels-photo-11079279.jpeg", "fotos/horizontal/03.jpg"),
    ("https://images.pexels.com/photos/5091141/pexels-photo-5091141.jpeg", "fotos/horizontal/04.jpg"),
    ("https://images.pexels.com/photos/1546890/pexels-photo-1546890.jpeg", "fotos/horizontal/05.jpg"),
    ("https://images.pexels.com/photos/1089570/pexels-photo-1089570.jpeg", "fotos/horizontal/06.jpg"),
    ("https://images.pexels.com/photos/730191/pexels-photo-730191.jpeg", "fotos/horizontal/07.jpg"),
    ("https://images.pexels.com/photos/8836426/pexels-photo-8836426.jpeg", "fotos/horizontal/08.jpg"),
    ("https://images.pexels.com/photos/1619572/pexels-photo-1619572.jpeg", "fotos/horizontal/09.jpg"),
    ("https://images.pexels.com/photos/6231588/pexels-photo-6231588.jpeg", "fotos/horizontal/10.jpg"),
    ("https://images.pexels.com/photos/8425210/pexels-photo-8425210.jpeg", "fotos/vertical/01.jpg"),
    ("https://images.pexels.com/photos/8105039/pexels-photo-8105039.jpeg", "fotos/vertical/02.jpg"),
    ("https://images.pexels.com/photos/4959984/pexels-photo-4959984.jpeg", "fotos/vertical/03.jpg"),
    ("https://images.pexels.com/photos/28793164/pexels-photo-28793164.jpeg", "fotos/vertical/04.jpg"),
    ("https://images.pexels.com/photos/11374693/pexels-photo-11374693.jpeg", "fotos/vertical/05.jpg"),
    ("https://images.pexels.com/photos/8858950/pexels-photo-8858950.jpeg", "fotos/vertical/06.jpg"),
    ("https://images.pexels.com/photos/14090902/pexels-photo-14090902.jpeg", "fotos/vertical/07.jpg"),
    ("https://images.pexels.com/photos/11909323/pexels-photo-11909323.jpeg", "fotos/vertical/08.jpg"),
    ("https://images.pexels.com/photos/29843736/pexels-photo-29843736.jpeg", "fotos/vertical/09.jpg"),
    ("https://images.pexels.com/photos/11019175/pexels-photo-11019175.jpeg", "fotos/vertical/10.jpg")
]

if __name__ == "__main__":
    criar_pastas()
    for url, destino in downloads:
        baixar_arquivo(url, destino)
