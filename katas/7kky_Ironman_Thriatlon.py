def i_tri(s):
    if s == 0:
        return 'Starting Line... Good Luck!'
    elif s < 2.4:
        return {'Swim': f'{140.60 - s:.2f} to go!'}
    elif s < 114.4:
        return {'Bike': f'{140.60 - s:.2f} to go!'}
    elif s < 130.6:
        return {'Run': f'{140.60 - s:.2f} to go!'}
    elif s < 140.6:
        return {'Run': 'Nearly there!'}
    else:
        return "You're done! Stop running!"


print(i_tri(36))
#{'Bike':'104.60 to go!'})
# Test.assert_equals(i_tri(103),{'Bike':'37.60 to go!'})
# Test.assert_equals(i_tri(0),'Starting Line... Good Luck!')
# Test.assert_equals(i_tri(2),{'Swim':'138.60 to go!'})
# Test.assert_equals(i_tri(151),"You're done! Stop running!")