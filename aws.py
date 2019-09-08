import boto3
import csv
import json
import xlsxwriter
import os


def build_dataset():
    with open('credentials.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[0]
            secret_access_key = line[1]

    rekognition = boto3.client(
        "rekognition", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, region_name='us-east-1')

    frames = os.listdir('video_frames')

    workbook = xlsxwriter.Workbook('dataset.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Second')
    worksheet.write('B1', 'Image')
    worksheet.write('C1', 'Emotion')
    worksheet.write('D1', 'Confidence')

    currRow = 2

    for frame in frames:
        print(frame)
        photo = 'video_frames/' + frame
        with open(photo, 'rb') as source_image:
            source_bytes = source_image.read()
        response = rekognition.detect_faces(
            Image={'Bytes': source_bytes}, Attributes=['ALL'])

        worksheet.write('A%d' % currRow, frame.replace('.jpg', ''))

        maxEmotion = response['FaceDetails'][0]['Emotions']
        maxNum = 0.0
        for emotion in response['FaceDetails'][0]['Emotions']:
            if emotion['Confidence'] > maxNum:
                maxNum = emotion['Confidence']
                maxEmotion = emotion['Type']

        worksheet.write('B%d' % currRow, frame)
        worksheet.write('C%d' % currRow, maxEmotion)
        worksheet.write('D%d' % currRow, maxNum)
        currRow += 1

    workbook.close()
