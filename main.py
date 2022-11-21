# This is a sample Python script.
import pandas as pd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.pyplot import figure

cols = ['Request quantity', 'Time per request', 'Full time']

image_search_time = 3
sic_answ_time = 10
cis_delay_time = 1
uls_delay_time = 1
cis_delay_count = 1
uls_delay_count = 1

rows = 50



add_select_cis_time_manual = pd.DataFrame({
    'Image searching time': np.arange(0, image_search_time * 4, (image_search_time * 4)/rows),
    'Time delay in function': np.arange(0, cis_delay_time * 7, (cis_delay_time * 7)/rows),
    'Operation time': np.arange(0, 0.1 * 11, (0.1 * 11)/rows)
})
add_select_cis_time_manual['All time per request'] = add_select_cis_time_manual['Image searching time']+add_select_cis_time_manual['Time delay in function']+add_select_cis_time_manual['Operation time']


xls_search_time_manual = pd.DataFrame({
    'Image searching time': np.arange(0, image_search_time * 4, (image_search_time * 4)/rows),
    'Time delay in function': np.arange(0, cis_delay_time * 3, (cis_delay_time * 3)/rows),

    'Operation time': np.arange(0, 0.1 * 2, (0.1 * 2)/rows),
    'CIS answer time': np.arange(0, sic_answ_time * 1, (sic_answ_time * 1)/rows),
})
xls_search_time_manual['All time per request'] = xls_search_time_manual['Image searching time']+xls_search_time_manual['Time delay in function']+xls_search_time_manual['Operation time']+xls_search_time_manual['CIS answer time']

time_data = pd.DataFrame({'Request quantity':[i for i in range(1,50,3)]})



sum_df = pd.DataFrame({
    'Image searching time': add_select_cis_time_manual['Image searching time']+xls_search_time_manual['Image searching time'],
    'Time delay in function': add_select_cis_time_manual['Time delay in function']+xls_search_time_manual['Time delay in function'],
    'ULS/ CIS answer time': np.arange(0, 10 * 2, (10 * 2)/rows),
    'Human productivity': np.arange(20, 120, (120-20)/rows),
    'Full Time per operation': add_select_cis_time_manual['All time per request']+xls_search_time_manual['All time per request']
})











#DASHBOARD
st.title('Working with CIS and ULS databases')
#st.write(sum_df)
#st.write(add_select_cis_time_manual)
st.title('Project of automation tool')




#KEY tech part
st.header('Key technologies')
#st.write('For this project may be used next technologies:')
parser = st.container()
cnn = st.container()
anchor_image = st.container()
parser, cnn, anchor_image = st.columns(3)

with parser:
    st.subheader('Web Parsing')
    st.write('Searching through the CIS database of existing items by using and analyzing the html code of the CIS page.')
with cnn:
    st.subheader('Neural Networks')
    st.write('Using Neural Networks for search and detection work windows (ULS, CISnet) ant it`s element on desktop ')
with anchor_image:
    st.subheader('System control')
    st.write('Automatic system interface control without human control')


# TECH DETAILS

st.header('Technology details')

## SELENIUM
st.header('Selenium WebDriver')
selenium_pars = st.container()

with selenium_pars:
    #sel_logo = Image.open('selenium_structure.jpg')
    sel_text, sel_img = st.columns(2)
    sel_logo = Image.open('C:/Users/Anastasia/PycharmProjects/DPMN_ML/scientificProject/image/Selenium_Logo.jpg')
    sel_text.write('Parsing will be realized with Selenium. Selenium uses browser automation APIs provided by'
                   ' browser vendors to control the browser and run tests. This is as if a real user is operating '
                   'the browser. Since WebDriver does not require its API to be compiled with application code; '
                   'It is not intrusive. Hence, you are testing the same application which you push live.')
    sel_img.image(sel_logo)
    #st.image(Image.open('C:/Users/Anastasia/PycharmProjects/DPMN_ML/scientificProject/selenium_structure.jpg'))
    st.subheader('Selenium work details')
    sel_str = Image.open('C:/Users/Anastasia/PycharmProjects/DPMN_ML/scientificProject/selenium_structure.jpg')
    st.image(sel_str)

## NEURAL NETWORKS
st.header('Neural Networks')
st.subheader('Neural networks using for search windows and interface elements on screen')
nn_search = st.container()

with nn_search:
    nn_text, nn_img = st.columns(2)
    nn_image = Image.open('C:/Users/Anastasia/PycharmProjects/DPMN_ML/scientificProject/image/cnn_work.png')
    nn_text.write('Convolutional Neural Network (ConvNet/CNN) is a Deep Learning algorithm that can take in an input'
                  ' image, assign importance (learnable weights and biases) to various objects in the image, '
                  'and be able to differentiate one from the other. ')
    nn_img.image(nn_image)
    st.subheader('In project "CNN" technology will be adapted for analize the video from screen and searching the '
                 'coordinates of interface elements')
    elem_img = st.container()
    elem_txt, elem_img = st.columns(2)
    elem_txt.write('Algorithm will be searching parts of interface like these, calculate the coordinates, and'
                   ' send this information '
                   'to the system control algorithm. ')
    with elem_img:
        elem_img.image(Image.open('C:/Users/Anastasia/PycharmProjects/DPMN_ML/scientificProject/image/cwr2_left_win.png'))
        elem_img.image(
            Image.open('C:/Users/Anastasia/PycharmProjects/DPMN_ML/scientificProject/image/cis_first_pos.png'))
        elem_img.image(
            Image.open('C:/Users/Anastasia/PycharmProjects/DPMN_ML/scientificProject/image/cis_found.png'))


## SYSTEM CONTROL
st.header('System control algorithms')
st.subheader('Algorithm that used for emulation of pc user activity ')
st.subheader('Now the library "PyAutoGui" is used to solve this problem.')
gui_txt = st.container()
gui_txt, gui_img = st.columns(2)
gui_txt.write('test')
gui_img.image(Image.open('C:/Users/Anastasia/PycharmProjects/DPMN_ML/scientificProject/image/autogui.jpg'))
with gui_txt:
    st.subheader('PyAutoGUI has several features:')
    st.write('🚩 Moving the mouse and clicking in the windows of other applications.')
    st.write('🚩 Sending keystrokes to applications (for example, to fill out forms).')
    st.write('🚩 Take screenshots, and given an image (for example, of a button or checkbox), and find it on the screen.')
    st.write('🚩 Locate an application’s window, and move, resize, maximize, minimize, or close it (Windows-only, currently')

# PLOTS


st.header('Work speed of algorithm (in plot)')

info_metric =st.container()
info_fig, info_metric = st.columns(2)

### SLIDERS
man_speed = st.slider('Manual working speed', 5, 60, 44)
cis_time = 8
uls_time = 3
program_delay_max = round(max([add_select_cis_time_manual['Time delay in function']+ add_select_cis_time_manual['Operation time']+add_select_cis_time_manual['Image searching time']+xls_search_time_manual['Time delay in function']+ xls_search_time_manual['Operation time']+xls_search_time_manual['Image searching time']][0]))
program_delay_min = round(min([add_select_cis_time_manual['Time delay in function']+ add_select_cis_time_manual['Operation time']+add_select_cis_time_manual['Image searching time']+xls_search_time_manual['Time delay in function']+ xls_search_time_manual['Operation time']+xls_search_time_manual['Image searching time']][0]))

algorithm_speed = st.slider('Automatic working speed', program_delay_min, program_delay_max, 25)
st.write(program_delay_max)

#plot

labels = ['Per hour', 'Per day', 'Per work week', 'Per work month']
human_means = [360/int((70 - man_speed)),7*360/int((70 - man_speed)),5*7*360/int((70 - man_speed)),25*7*360/int((70 - man_speed)),]
comp_means = [360/int((37 - algorithm_speed)),7*360/int((37 - algorithm_speed)),5*7*360/int((37 - algorithm_speed)),25*7*360/int((37 - algorithm_speed))]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, human_means, width, label='human')
rects2 = ax.bar(x + width/2, comp_means, width, label='algorithm')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of applications')
ax.set_title('The number of processed applications for different periods of time. Human vs algorithm.')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
st.pyplot(fig)








