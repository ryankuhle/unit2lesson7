'''
100 out of 10,000 women at age forty have breast cancer
out of those 100, 80 of them will get a positive mammogram
of the remaining 9900 women, 950 will not have breast cancer but will get a positive mammogram

Solve: What percentage of women with positive mammograms will actually have  breast cancer?

Total women with positive mammograms is 1030
total women with breast cancer is 80
what percentage is 80 of 1030

Answer: 7.8%
'''

def cancerMath(total_woman):
    woman_w_cancer = int(total_woman * .01)
    pos_mammogram_w_cancer = int(woman_w_cancer * .8)
    pos_mammogram_without_cancer = int((total_woman - woman_w_cancer) * .096)
    total_pos_mammogram = int(pos_mammogram_without_cancer + pos_mammogram_w_cancer)
    percentage = pos_mammogram_w_cancer / float(total_pos_mammogram)
    print "Women with cancer: %s" % woman_w_cancer
    print "Women with cancer and positive mammogram: %s" % pos_mammogram_w_cancer
    print "Women without cancer and positive mammogram: %s" % pos_mammogram_without_cancer
    print "Women with positive mammogram: %s" % total_pos_mammogram
    print "Percentage of positive mammograms with breast cancer: {0:.1%}".format(percentage)

x = int(raw_input("How many total women are there? "))
cancerMath(x)
