from xml.dom.minidom import Document

class XMLNode:
    def __init__(self, nodetype, attrDict={}, children=[], value='', cdata=False):
        self.nodetype = nodetype
        self.attributesDictionary = attrDict
        self.children = children
        self.value = value
        self.cdata = cdata

    def toXMLElement(self, xmlDocument):
        result = xmlDocument.createElement(self.nodetype)
        for key in self.attributesDictionary.keys():
            result.setAttribute(key, self.attributesDictionary[key])
        if self.nodetype == 'text' or len(self.value) > 0:
            temp = Text()
            if self.cdata and len(self.value) > 0:
                temp = CDATASection()
            temp.data = self.value
            result.appendChild(temp)
        for child in self.children:
            result.appendChild(child.toXMLElement(xmlDocument))
        return result

class MoodleXMLMultipleChoiceQuestion:
    def __init__(self, name, questiontext, answers, feedback=""):
        self.name = name
        self.questiontext = questiontext
        self.answers = answers
        self.feedback = feedback

    def toXML(self, xmlDocument):
        question = xmlDocument.createElement("question")
        question.setAttribute("type", "multichoice")

        name_node = xmlDocument.createElement("name")
        name_text = xmlDocument.createElement("text")
        name_text.appendChild(xmlDocument.createTextNode(self.name))
        name_node.appendChild(name_text)
        question.appendChild(name_node)

        questiontext_node = xmlDocument.createElement("questiontext")
        questiontext_node.setAttribute("format", "html")
        text_node = xmlDocument.createElement("text")
        text_node.appendChild(xmlDocument.createCDATASection(self.questiontext))
        questiontext_node.appendChild(text_node)
        question.appendChild(questiontext_node)

        for answer_text, fraction in self.answers:
            answer_node = xmlDocument.createElement("answer")
            answer_node.setAttribute("fraction", str(fraction))
            answer_text_node = xmlDocument.createElement("text")
            answer_text_node.appendChild(xmlDocument.createTextNode(answer_text))
            answer_node.appendChild(answer_text_node)
            question.appendChild(answer_node)

        feedback_node = xmlDocument.createElement("generalfeedback")
        feedback_text = xmlDocument.createElement("text")
        feedback_text.appendChild(xmlDocument.createTextNode(self.feedback))
        feedback_node.appendChild(feedback_text)
        question.appendChild(feedback_node)

        return question

class MoodleXMLFile:
    def __init__(self):
        self.categories = []

    def addCategory(self, name, questions):
        self.categories.append({"name": name, "questions": questions})

    def toXMLDocument(self):
        document = Document()
        quiz = document.createElement("quiz")
        document.appendChild(quiz)

        for category in self.categories:
            category_node = document.createElement("question")
            category_node.setAttribute("type", "category")
            category_text = document.createElement("text")
            category_text.appendChild(document.createTextNode(category["name"]))
            category_node.appendChild(category_text)
            quiz.appendChild(category_node)

            for question in category["questions"]:
                quiz.appendChild(question.toXML(document))

        return document
