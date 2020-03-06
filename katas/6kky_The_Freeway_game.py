def freeway_game(dist_km_to_exit, my_speed_kph, other_cars):
    count = 0
    my_car_time = dist_km_to_exit / my_speed_kph * 60
    for car in other_cars:                       
        other_car_time = (dist_km_to_exit / car[1] * 60) + car[0]        
        if car[0] <= 0 and my_car_time < other_car_time:               
            count += 1         
        elif car[0] > 0 and my_car_time > other_car_time:
            count -= 1       

    return count
