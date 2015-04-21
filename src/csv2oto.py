# -*- coding: utf-8 -*-
import os
import sys
import codecs

# import my py-tools. (Get it from 'https://github.com/kilfu0701/py-tools')
#sys.path.append('/Users/fu/Desktop/github/py-tools')

#try:
#    from debug.debug import Debug as D
#    d = D(level=4, color=True, types='unicode')
#except:
#    print '** No debug module'
#    sys.exit()


CSV_DIR = 'csv/'
WAV_DIR = 'wav/'
CSV_FILE = 'output_japanese.csv'
AUDIO_EXT = '.wav'
OUTPUT_INI = 'oto_ja.ini'

# 單獨音
single_dict = {}
# 連續音
continuous_dict = {}


## Load csv file
csv_path = CSV_DIR + CSV_FILE
#d.info('Read csv =', csv_path)

with codecs.open(csv_path, 'r', 'utf8') as f:
    lines = f.readlines()

    #d.info('Total Lines =', len(lines))

    with codecs.open(OUTPUT_INI, 'w+', encoding='utf8') as out_file:

        out_file.write( u'\n'.join([
            u';license CC-BY 3.0',
            u';authon:MGdesigner，宇圻，kilfu0701',
            u';編輯注意事項',
            u';1.註解請用分號',
            u';2.同一個發音有需要可以用alias',
            u';================',
            u';==單獨音區======',
            u';================'
        ]) + '\n' )

        ## [單獨音]
        for i in lines[:]:
            jp_str, ipa, naming = i.strip().split(u',')

            ## 取出第一個
            symbols = naming.split('-')
            ipa_symbols = ipa.split('-')

            if len(ipa_symbols) == 1 and ipa_symbols[0] == '':
                first_ipa = None
            else:
                first_ipa = ipa_symbols[0]

            if len(symbols) != 0:
                if symbols[0] not in single_dict:

                    single_dict[symbols[0]] = {
                        'jp': jp_str,
                        'ipa': first_ipa
                    }

                else:
                    ## skip 非單獨音
                    continue


            ## select naming string name for *.wav
            param = [jp_str, '', '', '', '', '']
            out_file.write( naming + '.wav=' + u','.join(param) + '\n'  )

            if first_ipa is None:
                line = ';' + naming + '.wav=,,,,,\n'
            else:
                line = naming + '.wav=' + first_ipa + ',,,,,\n'

            out_file.write(line)

        ## [單獨音] End


        ## [連續音]
        out_file.write( u'\n'.join([
            u'',
            u';================',
            u';==連續音區======',
            u';================'
        ]) + '\n' )

        for i in lines[:]:
            # split as ['んぐぇんぐぉぐ', 'n--n--gɯ', 'N-Gwe-N-Gwo-Gu']
            jp_str, ipa, naming = i.strip().split(u',')

            symbols = naming.split('-')
            #ipa_symbols = ipa.split('-')

            ## skip 單獨音
            if len(symbols) == 1:
                continue

            for i in xrange(len(symbols) - 1):
                line = naming + '.wav=' + ' '.join([symbols[i][-1].lower(), single_dict[symbols[i + 1]]['jp'] ]) + ',,,,,\n'
                out_file.write(line)


print 'Output file:', OUTPUT_INI
print 'Parse Done.'

#d.info('Output file:', OUTPUT_INI)
#d.info('Parse Done.')

