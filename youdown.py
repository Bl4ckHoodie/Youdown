#https://www.youtube.com/watch?v=_eFad7AGWdM
#youDown - 


#from pytube import Playlist
#playlist = Playlist('https://www.youtube.com/watch?v=58PpYacL-VQ&list=UUd6MoB9NC6uYN2grvUNT-Zg')
#print('Number of videos in playlist: %s' % len(playlist.video_urls))
#playlist.download_all()
import wx
from pytube import YouTube
from multiprocessing import Process, Queue

class mainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(mainFrame, self).__init__(parent, title= title, size=(400,350))
        self.Center()
        panel = wx.Panel(self)
        s1="                                      _ .-') _                 (`\ .-') /`     .-') _"  
        s2="                                     ( (  OO) )                 `.( OO ),'    ( OO ) )" 
        s3="  ,--.   ,--..-'),-----.  ,--. ,--.   \     .'_  .-'),-----. ,--./  .--.  ,--./ ,--,'  "
        s4="   \  `.'  /( OO'  .-.  ' |  | |  |   ,`'--..._)( OO'  .-.  '|      |  |  |   \ |  |\  "
        s5=" .-')     / /   |  | |  | |  | | .-') |  |  \  '/   |  | |  ||  |   |  |, |    \|  | ) "
        s6="(OO  \   /  \_) |  |\|  | |  |_|( OO )|  |   ' |\_) |  |\|  ||  |.'.|  |_)|  .     |/ " 
        s7=" |   /  /\_   \ |  | |  | |  | | `-' /|  |   / :  \ |  | |  ||         |  |  |\    |   "
        s8=" `-./  /.__)   `'  '-'  '('  '-'(_.-' |  '--'  /   `'  '-'  '|   ,'.   |  |  | \   |  " 
        s9="   `--'          `-----'   `-----'    `-------'      `-----' '--'   '--'  `--'  `--'  "
        s = s1+"\n"+s2+"\n"+s3+"\n"+s4+"\n"+s5+"\n"+s6+"\n"+s7+"\n"+s8+"\n"+s9
        self.lbl = wx.StaticText(panel, label = "YouDown-", pos = (100,250))
        fontTitle = wx.Font(24, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
        self.lbl.SetLabel(s)
        self.lbl.SetFont(fontTitle)
        self.l = wx.StaticText(panel,label = "YOUTUBE DOWNLOADER", pos = (100,10))
        fontSlogan = wx.Font(12, wx.ROMAN, wx.ITALIC,wx.BOLD)
        self.txt = wx.TextCtrl(panel,size=(180,20), pos=(110,60))
        self.b = wx.Button(panel, label = 'Download', pos = (150,150), size=(100,40))
        self.b.Bind(wx.EVT_BUTTON, self.download)
    def download(self, e):
        st = self.txt.GetValue()
        if(st != ''):
            url = YouTube(str(st))
            print("Downloading...\n"+url.title)
            self.b.Disable()
            queue = Queue()
            video = url.streams.get_highest_resolution()
            Process(target= video.download('downloads'), args=())
            print("Finished...")
            self.txt.SetValue('')
            self.b.Enable()
        


program = wx.App()
window = mainFrame(None,title='YouDown')
window.Show()
program.MainLoop()
