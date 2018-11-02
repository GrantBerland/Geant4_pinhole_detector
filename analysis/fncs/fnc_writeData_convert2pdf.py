

import subprocess

def writeData_convert2pdf(fileName, det_attributes):

    with open('/home/grant/Documents/Research/Marshall_Research/electron_detector/results/tmp.txt','w') as f:
        f.write('Detector 1 thickness: %f um\n' % det_attributes[0])
        f.write('Detector 2 thickness: %f um\n' % det_attributes[1])
        f.write('Gap between detectors: %f mm\n' % det_attributes[2])
        f.write('Window thickness: %f um\n' % det_attributes[3])
        f.write('Gap between window and detector 1: %f mm\n' % det_attributes[4])


    bashConvert2PDF = 'unoconv ../results/tmp.txt'
    process = subprocess.Popen(bashConvert2PDF.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    msg, error = process.communicate()
    print('Writing file...')

    if error is not None:
        print('Error in converting tmp.txt to tmp.pdf')

    # error Checks

    bashCombinePDFs = 'pdftk ../results/' + str(fileName) + '.pdf ../results/tmp.pdf output ../results/' + str(fileName) + '_D.pdf'
    process = subprocess.Popen(bashCombinePDFs.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    msg, error = process.communicate()
    print('Converting to PDF...')

    if error is not None:
        print('Error in combining plot and data pdfs')

    bashCleanTmpFiles = 'rm ../results/tmp.txt ../results/tmp.pdf ../results/' + str(fileName) + '.pdf'
    process = subprocess.Popen(bashCleanTmpFiles.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    msg, error = process.communicate()

    if error is not None:
        print('Error in removing tmp files')
