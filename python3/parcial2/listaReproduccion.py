from video import *

class ListaReproduccion:
    prox_nro = int(0)
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__nro = ListaReproduccion.get_prox_nro()
        self.__videos = []


    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombreValor):
        self.__nombre = nombreValor


    @property
    def nro(self):
        return self.__nro
    @nro.setter
    def nro(self,nroValor):
        self.__nro = nroValor

    @property
    def cantidad_videos(self):
        return len(self.videos)






    @property
    def videos(self):
        return self.__videos
    @videos.setter
    def videos(self,videosValor):
        self.__videos = videosValor


    def add_video(self, video: Video):
        self.__videos.append(video)

    def remove_video(self, video: Video):
        self.__videos.remove(video)
    
    
    @classmethod
    def get_prox_nro(cls):
        cls.prox_nro += 1
        return cls.prox_nro

    



    
        
