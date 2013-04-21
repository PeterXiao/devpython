__author__ = 'Administrator'
#pip install tornado
import win32file
def frrespaceodisk(dir):
      sectorsPerCluster, bytesPerSector, numFreeClusters, totalNumClusters = win32file.GetDiskFreeSpace(dir)
      print( "FreeSpace:", (numFreeClusters * sectorsPerCluster * bytesPerSector) /(1024 * 1024), "MB")

dir = "c:\\"

frrespaceodisk(dir)