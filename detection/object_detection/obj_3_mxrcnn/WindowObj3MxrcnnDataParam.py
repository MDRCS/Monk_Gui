import os
import sys
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class WindowObj3MxrcnnDataParam(QtWidgets.QWidget):

    backward_3_mxrcnn = QtCore.pyqtSignal();
    forward_data_preproc = QtCore.pyqtSignal();

    def __init__(self):
        super().__init__()
        self.title = 'Mxrcnn - Training Data Param'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 500
        self.cfg_setup();
        self.initUI();


    def cfg_setup(self):
        if(os.path.isfile("obj_3_mxrcnn.json")):
            with open('obj_3_mxrcnn.json') as json_file:
                self.system = json.load(json_file)
        else:
            self.system = {};
            self.system["anno_type"] = "monk"

            self.system["monk_root_dir"] = "Monk_Object_Detection/example_notebooks/sample_dataset/kangaroo/";
            self.system["monk_img_dir"] = "Images";
            self.system["monk_anno_file"] = "train_labels.csv";

            self.system["voc_root_dir"] = "Monk_Object_Detection/example_notebooks/sample_dataset/kangaroo/";
            self.system["voc_img_dir"] = "Images";
            self.system["voc_anno_dir"] = "";

            self.system["coco_root_dir"] = "Monk_Object_Detection/example_notebooks/sample_dataset/";
            self.system["coco_coco_dir"] = "kangaroo";
            self.system["coco_img_dir"] = "Images";

            self.system["batch_size"] = "4";

            self.system["img_short_side"] = "600";
            self.system["img_long_side"] = "1000";
            self.system["mean"] = "123.68, 116.779, 103.939";
            self.system["std"] = "1.0, 1.0, 1.0";

            self.system["model"] = "resnet50";
            self.system["use_pretrained"] = "yes";
            self.system["use_gpu"] = "yes";
            self.system["devices"] = "0";
            
            self.system["lr"] = "0.001";
            self.system["lr_decay_epoch"] = "2, 4";
            self.system["epochs"] = "5";
            self.system["log_interval"] = "100";
            self.system["output_model_name"] = "model_resnet50";

            with open('obj_3_mxrcnn.json', 'w') as outfile:
                json.dump(self.system, outfile)



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height);


        # Backward
        self.b1 = QPushButton('Back', self)
        self.b1.move(500,450)
        self.b1.clicked.connect(self.backward)

        # Forward
        self.b2 = QPushButton('Next', self)
        self.b2.move(600,450)
        self.b2.clicked.connect(self.forward);

        # Quit
        self.b3 = QPushButton('Quit', self)
        self.b3.move(700,450)
        self.b3.clicked.connect(self.close)

        
        self.tb1 = QTextEdit(self)
        self.tb1.move(20, 20)
        self.tb1.resize(400, 450)
        self.tb1.setText(self.monk_format());
        self.tb1.setReadOnly(True)
        

        
        self.r1 = QRadioButton("Monk format", self)
        if self.system["anno_type"] == "monk":
            self.r1.setChecked(True)
        self.r1.move(430,20)
        self.r1.toggled.connect(self.monk);

        self.r2 = QRadioButton("VOC format", self)
        if self.system["anno_type"] == "voc":
            self.r2.setChecked(True)
        self.r2.move(560,20)
        self.r2.toggled.connect(self.voc);

        self.r3 = QRadioButton("COCO format", self)
        if self.system["anno_type"] == "coco":
            self.r3.setChecked(True)
        self.r3.move(670,20)
        self.r3.toggled.connect(self.coco);


        
        self.m = [];
        self.m_l1 = QLabel(self);
        self.m_l1.setText("1. root:");
        self.m_l1.move(450, 70);
        self.m.append(self.m_l1);

        self.m_b1 = QPushButton('Select Folder', self)
        self.m_b1.move(550,70)
        self.m_b1.clicked.connect(self.select_root_dataset)
        self.m.append(self.m_b1);

        self.m_tb1 = QTextEdit(self)
        self.m_tb1.move(450, 100)
        self.m_tb1.resize(300, 50)
        self.m_tb1.setText(self.system["monk_root_dir"]);
        self.m_tb1.setReadOnly(True)
        self.m.append(self.m_tb1);


        self.m_l2 = QLabel(self);
        self.m_l2.setText("2. img_dir:");
        self.m_l2.move(450, 180);
        self.m.append(self.m_l2);

        self.m_b2 = QPushButton('Select Folder', self)
        self.m_b2.move(550,180)
        self.m_b2.clicked.connect(self.select_img_dir)
        self.m.append(self.m_b2);

        self.m_tb2 = QTextEdit(self)
        self.m_tb2.move(450, 210)
        self.m_tb2.resize(300, 50)
        self.m_tb2.setText(self.system["monk_img_dir"]);
        self.m_tb2.setReadOnly(True)
        self.m.append(self.m_tb2);

        self.m_l3 = QLabel(self);
        self.m_l3.setText("3. anno_file:");
        self.m_l3.move(450, 280);
        self.m.append(self.m_l3);

        self.m_b3 = QPushButton('Select File', self)
        self.m_b3.move(550, 280)
        self.m_b3.clicked.connect(self.select_anno_file)
        self.m.append(self.m_b3);

        self.m_tb3 = QTextEdit(self)
        self.m_tb3.move(450, 310)
        self.m_tb3.resize(300, 50)
        self.m_tb3.setText(self.system["monk_anno_file"]);
        self.m_tb3.setReadOnly(True)
        self.m.append(self.m_tb3);

        self.m_l4 = QLabel(self);
        self.m_l4.setText("4. batch_size:");
        self.m_l4.move(450, 380);
        self.m.append(self.m_l4);

        self.m_e4 = QLineEdit(self)
        self.m_e4.move(550, 380);
        self.m_e4.setText(self.system["batch_size"]);
        self.m_e4.resize(200, 25);
        self.m.append(self.m_e4);
        



        
        self.v = [];
        self.v_l1 = QLabel(self);
        self.v_l1.setText("1. root:");
        self.v_l1.move(450, 70);
        self.v.append(self.v_l1);


        self.v_b1 = QPushButton('Select Folder', self)
        self.v_b1.move(550,70)
        self.v_b1.clicked.connect(self.select_root_dataset)
        self.v.append(self.v_b1);

        self.v_tb1 = QTextEdit(self)
        self.v_tb1.move(450, 100)
        self.v_tb1.resize(300, 50)
        self.v_tb1.setText(self.system["voc_root_dir"]);
        self.v_tb1.setReadOnly(True)
        self.v.append(self.v_tb1);

        self.v_l2 = QLabel(self);
        self.v_l2.setText("2. img_dir:");
        self.v_l2.move(450, 180);
        self.v.append(self.v_l2);

        self.v_b2 = QPushButton('Select Folder', self)
        self.v_b2.move(550,180)
        self.v_b2.clicked.connect(self.select_img_dir)
        self.v.append(self.v_b2);

        self.v_tb2 = QTextEdit(self)
        self.v_tb2.move(450, 210)
        self.v_tb2.resize(300, 50)
        self.v_tb2.setText(self.system["voc_img_dir"]);
        self.v_tb2.setReadOnly(True)
        self.v.append(self.v_tb2);

        self.v_l3 = QLabel(self);
        self.v_l3.setText("3. anno_dir:");
        self.v_l3.move(450, 280);
        self.v.append(self.v_l3);

        self.v_b3 = QPushButton('Select Folder', self)
        self.v_b3.move(550, 280)
        self.v_b3.clicked.connect(self.select_anno_dir)
        self.v.append(self.v_b3);

        self.v_tb3 = QTextEdit(self)
        self.v_tb3.move(450, 310)
        self.v_tb3.resize(300, 50)
        self.v_tb3.setText(self.system["voc_anno_dir"]);
        self.v_tb3.setReadOnly(True)
        self.v.append(self.v_tb3);

        self.v_l4 = QLabel(self);
        self.v_l4.setText("4. batch_size:");
        self.v_l4.move(450, 380);
        self.v.append(self.v_l4);

        self.v_e4 = QLineEdit(self)
        self.v_e4.move(550, 380);
        self.v_e4.setText(self.system["batch_size"]);
        self.v_e4.resize(200, 25);
        self.v.append(self.v_e4);



        self.c = [];
        self.c_l1 = QLabel(self);
        self.c_l1.setText("1. root:");
        self.c_l1.move(450, 70);
        self.c.append(self.c_l1);

        self.c_b1 = QPushButton('Select Folder', self)
        self.c_b1.move(550,70)
        self.c_b1.clicked.connect(self.select_root_dataset)
        self.c.append(self.c_b1);

        self.c_tb1 = QTextEdit(self)
        self.c_tb1.move(450, 100)
        self.c_tb1.resize(300, 50)
        self.c_tb1.setText(self.system["coco_root_dir"]);
        self.c_tb1.setReadOnly(True)
        self.c.append(self.c_tb1);


        self.c_l2 = QLabel(self);
        self.c_l2.setText("2. coco_dir:");
        self.c_l2.move(450, 180);
        self.c.append(self.c_l2);

        self.c_b2 = QPushButton('Select Folder', self)
        self.c_b2.move(550,180)
        self.c_b2.clicked.connect(self.select_coco_dir)
        self.c.append(self.c_b2);

        self.c_tb2 = QTextEdit(self)
        self.c_tb2.move(450, 210)
        self.c_tb2.resize(300, 50)
        self.c_tb2.setText(self.system["coco_coco_dir"]);
        self.c_tb2.setReadOnly(True)
        self.c.append(self.c_tb2);


        self.c_l3 = QLabel(self);
        self.c_l3.setText("3. img_dir:");
        self.c_l3.move(450, 280);
        self.c.append(self.c_l3);

        self.c_b3 = QPushButton('Select Folder', self)
        self.c_b3.move(550,280)
        self.c_b3.clicked.connect(self.select_img_dir)
        self.c.append(self.c_b3);

        self.c_tb3 = QTextEdit(self)
        self.c_tb3.move(450, 310)
        self.c_tb3.resize(300, 50)
        self.c_tb3.setText(self.system["coco_img_dir"]);
        self.c_tb3.setReadOnly(True)
        self.c.append(self.c_tb3);

        self.c_l4 = QLabel(self);
        self.c_l4.setText("4. batch_size:");
        self.c_l4.move(450, 380);
        self.c.append(self.c_l4);

        self.c_e4 = QLineEdit(self)
        self.c_e4.move(550, 380);
        self.c_e4.setText(self.system["batch_size"]);
        self.c_e4.resize(200, 25);
        self.c.append(self.c_e4);

    

        if self.system["anno_type"] == "monk":
            self.monk();
        elif self.system["anno_type"] == "voc":
            self.voc();
        else:
            self.coco();
        


        

    def monk(self):
        self.tb1.setText(self.monk_format());
        for x in self.m:
            x.show();
        for x in self.v:
            x.hide();
        for x in self.c:
            x.hide();


    def voc(self):
        self.tb1.setText(self.voc_format());
        for x in self.m:
            x.hide();
        for x in self.v:
            x.show();
        for x in self.c:
            x.hide();


    def coco(self):
        self.tb1.setText(self.coco_format());
        for x in self.m:
            x.hide();
        for x in self.v:
            x.hide();
        for x in self.c:
            x.show();




    def select_root_dataset(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folderName = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", os.getcwd())
        if self.r1.isChecked():
            self.m_b1.setText("Selected");
            self.m_tb1.setText(folderName);
            self.system["monk_root_dir"] = folderName;
        if self.r2.isChecked():
            self.v_b1.setText("Selected");
            self.v_tb1.setText(folderName);
            self.system["voc_root_dir"] = folderName;
        if self.r3.isChecked():
            self.c_b1.setText("Selected");
            self.c_tb1.setText(folderName);
            self.system["coco_root_dir"] = folderName;
        


    def select_coco_dir(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folderName = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", self.system["coco_root_dir"])
        folderName = folderName.split("/")[-1];
        self.v_b2.setText("Selected");
        self.v_tb2.setText(folderName);
        self.system["coco_coco_dir"] = folderName;



    def select_img_dir(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        if self.r1.isChecked():
            folderName = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", self.system["monk_root_dir"])
        if self.r2.isChecked():
            folderName = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", self.system["voc_root_dir"])
        if self.r3.isChecked():
            folderName = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", 
                self.system["coco_root_dir"] + "/" + self.system["coco_coco_dir"])

        folderName = folderName.split("/")[-1];
        if self.r1.isChecked():
            self.m_b2.setText("Selected");
            self.m_tb2.setText(folderName);
            self.system["monk_img_dir"] = folderName;
        if self.r2.isChecked():
            self.v_b2.setText("Selected");
            self.v_tb2.setText(folderName);
            self.system["voc_img_dir"] = folderName;
        if self.r3.isChecked():
            self.c_b3.setText("Selected");
            self.c_tb3.setText(folderName);
            self.system["coco_img_dir"] = folderName;

        

    def select_anno_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", self.system["monk_root_dir"], 
                                                    "Monk Project Files (*.csv);;All Files (*)", options=options)
        if fileName:
            fileName = fileName.split("/")[-1];
            self.system["monk_anno_file"] = fileName;
            self.m_b3.setText("Selected");
            self.m_tb3.setText(fileName);


    def select_anno_dir(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folderName = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", self.system["voc_root_dir"])
        folderName = folderName.split("/")[-1];
        self.v_b3.setText("Selected");
        self.v_tb3.setText(folderName);
        self.system["voc_anno_dir"] = folderName;



    def forward(self):
        if self.r1.isChecked():
            self.system["anno_type"] == "monk";
            self.system["batch_size"] = self.m_e4.text();
        elif self.r2.isChecked():
            self.system["anno_type"] == "voc";
            self.system["batch_size"] = self.v_e4.text();
        else:
            self.system["anno_type"] == "coco";
            self.system["batch_size"] = self.c_e4.text();

        with open('obj_3_mxrcnn.json', 'w') as outfile:
            json.dump(self.system, outfile)


        self.forward_data_preproc.emit();



    def backward(self):
        if self.r1.isChecked():
            self.system["anno_type"] == "monk";
            self.system["batch_size"] = self.m_e4.text();
        elif self.r2.isChecked():
            self.system["anno_type"] == "voc";
            self.system["batch_size"] = self.v_e4.text();
        else:
            self.system["anno_type"] == "coco";
            self.system["batch_size"] = self.c_e4.text();

        with open('obj_3_mxrcnn.json', 'w') as outfile:
            json.dump(self.system, outfile)

        self.backward_3_mxrcnn.emit();


    def monk_format(self):
        wr = "";
        wr += "Monk Type Data Format\n"
        wr += "Dataset Directory Structure\n\n";
        wr += "Parent_Directory (root)\n";
        wr += "      |\n";
        wr += "      |-----------Images (img_dir)\n";
        wr += "      |              |\n";
        wr += "      |              |------------------img1.jpg\n";
        wr += "      |              |------------------img2.jpg\n";
        wr += "      |              |------------------.........(and so on)\n";
        wr += "      |\n";
        wr += "      |\n";
        wr += "      |-----------train_labels.csv (anno_file)\n\n";
        wr += "Annotation file format\n";
        wr += "       | Id         | Labels                                 |\n";
        wr += "       | img1.jpg   | x1 y1 x2 y2 label1 x1 y1 x2 y2 label2  |\n";
        wr += "    Labels: xmin ymin xmax ymax label\n";
        wr += "    xmin, ymin - top left corner of bounding box\n";
        wr += "    xmax, ymax - bottom right corner of bounding box\n";


        return wr;


    def voc_format(self):
        wr = "";
        wr += "VOC Type Data Format\n"
        wr += "Dataset Directory Structure\n\n";
        wr += "Parent_Directory (root)\n";
        wr += "      |\n";
        wr += "      |-----------Images (img_dir)\n";
        wr += "      |              |\n";
        wr += "      |              |------------------img1.jpg\n";
        wr += "      |              |------------------img2.jpg\n";
        wr += "      |              |------------------.........(and so on)\n";
        wr += "      |\n";
        wr += "      |\n";
        wr += "      |-----------Annotations (anno_dir)\n";
        wr += "      |              |\n";
        wr += "      |              |------------------img1.xml\n";
        wr += "      |              |------------------img2.xml\n";
        wr += "      |              |------------------.........(and so on)\n";

        return wr;


    def coco_format(self):
        wr = "";
        wr += "COCO Type Data Format\n"
        wr += "Dataset Directory Structure\n\n";
        wr += "Parent_Directory (root_dir)\n";
        wr += "      |\n";
        wr += "      |------kangaroo (coco_dir)\n";
        wr += "      |         |\n";
        wr += "      |         |---Images (img_dir)\n";
        wr += "      |         |----|\n";
        wr += "      |              |-------------------img1.jpg\n";
        wr += "      |              |-------------------img2.jpg\n";
        wr += "      |              |------------------.........(and so on)\n";
        wr += "      |\n";
        wr += "      |\n";
        wr += "      |         |---annotations (anno_dir)\n";
        wr += "      |         |----|\n";
        wr += "      |              |--------------------instances_Images.json\n";
        wr += "      |              |--------------------classes.txt\n"
        wr += "\n";
        wr += "\n";
        wr += "    instances_Train.json -> In proper COCO format\n";
        wr += "    Note: Annotation file name too coincides against the set_dir\n";
        wr += "    classes.txt -> A list of classes in alphabetical order\n";

        return wr;


'''
app = QApplication(sys.argv)
screen = WindowObj3MxrcnnDataParam()
screen.show()
sys.exit(app.exec_())
'''


