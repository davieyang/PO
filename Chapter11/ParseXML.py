# encoding = utf-8
from xml.etree import ElementTree


class ParseXML(object):
    def __init__(self, xmlPath):
        self.xmlPath = xmlPath

    def getRoot(self):
        """
        获取XML文件的根节点对象，然后返回给调用者
        :return:
        """
        # 打开将要解析的XML文件
        tree = ElementTree.parse(self.xmlPath)
        return tree.getroot()

    def findNodeByName(self, parentNode, nodeName):
        """
        通过节点的名字获取节点对象
        :param parentNode:
        :param nodeName:
        :return:
        """
        nodes = parentNode.findall(nodeName)
        return nodes

    def getNodeofChildText(self, node):
        """
        获取节点node下所有子节点的节点名作为key，本节点作为value组成的字典对象
        :param node:
        :return:
        """
        childrenTextDict = {i.tag: i.text for i in list(node.iter())[1:]}
        # 上面代码等价于
        return childrenTextDict

    def getDataFromXml(self, nodename):
        """
        遍历获取到的所有nodename对象,取得需要的测试数据
        :param nodename:
        :return:
        """
        # 获取XML文档的根节点对象
        root = self.getRoot()
        # 获取根节点下所有名为nodename对象
        books = self.findNodeByName(root, nodename)
        dataList = []
        for nodename in books:
            childrenText = self.getNodeofChildText(nodename)
            dataList.append(childrenText)
        return dataList


if __name__ == "__main__":
    xml = ParseXML(r"F:\pubbookone\TestData\test_search_data.xml")
    datas = xml.getDataFromXml("test")
    for i in datas:
        print(i["testdata"], i["expectdata"])
