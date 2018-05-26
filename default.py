import sys
import xbmcplugin
import xbmcgui

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'Live TV')

url='http://185.105.4.188:1935/ltv/myStream/playlist.m3u8'

li = xbmcgui.ListItem('Live TV', iconImage='icon.pgn')

xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
