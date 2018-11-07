

import subprocess

def writeData_convert2pdf(fileName, det_attributes, stats):

    with open('/home/grant/Documents/Research/Marshall_Research/pinhole_detector/results/tmp.txt','w') as f:
        f.write('Pinhole radius: %f mm\n' % det_attributes[0])
        f.write('Gap between window and detector: %f mm\n' % det_attributes[1])
        f.write('Window thickness: %f um\n' % det_attributes[2])
        f.write('Shielding foil thickness: %f um\n' % det_attributes[3])
        f.write('--------------------------------\n')
        s = 'Theta Angle (degrees), Standard deviation (degrees):\n {0}'
        f.write(s.format(*stats))


    bashConvert2PDF = 'unoconv ../results/tmp.txt'
    process = subprocess.Popen(bashConvert2PDF.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    msg, error = process.communicate()
    print('Writing file...')

    if len(error) is not 0:
        print('Error in converting tmp.txt to tmp.pdf: ' + str(error))

    # error Checks

    bashCombinePDFs = 'pdftk ../results/' + str(fileName) + '.pdf ../results/tmp.pdf output ../results/' + str(fileName) + '_D.pdf'
    process = subprocess.Popen(bashCombinePDFs.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    msg, error = process.communicate()
    print('Converting to PDF...')

    if len(error) is not 0:
        print('Error in combining plot and data pdfs: ' + str(error))


    bashCleanTmpFiles = 'rm ../results/tmp.txt ../results/tmp.pdf ../results/' + str(fileName) + '.pdf'
    process = subprocess.Popen(bashCleanTmpFiles.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    msg, error = process.communicate()

    if len(error) is not 0:
        print('Error in removing tmp files: ' + str(error))
