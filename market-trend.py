import autoit
import pandas

#autoit.win_activate("How random can you be? | Lineae ex punctis")

autoit.mouse_move(920,700)
autoit.mouse_click()

spdata = pandas.read_csv(r'C:\Users\bmort\source\data\^GSPC2.csv')
for i in range(1,spdata['Close'].size + 1):
    if spdata['Close'][i] < spdata['Close'][i - 1]:
        autoit.send("{LEFT}") 
    else:
        autoit.send("{RIGHT}") 


autoit.mouse_move(85,70)
autoit.mouse_click()

autoit.mouse_move(920,770)
#autoit.mouse_click()
autoit.mouse_click()

for i in range(0,spdata['Close'].size + 1):
    if spdata['Open'][i] < spdata['Close'][i]:
        autoit.send("{LEFT}") 
    else:
        autoit.send("{RIGHT}")


