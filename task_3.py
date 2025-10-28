class PointsForPlace:
    
    @staticmethod
    def get_points_for_place(place):
        points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else: 
            points = 101 - place
            return points


class PointsForMeters:
    
    @staticmethod
    def get_points_for_meters(meters):
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = int(0.5 * meters)
            return points

class TotalPoints(PointsForPlace, PointsForMeters):

    def get_total_points(self, meters, place):
        place_points = super().get_points_for_place(place)
        meters_points = super().get_points_for_meters(meters)
        if type(place_points) == str or isinstance(meters_points, str):
            total = f"{place_points}\n{meters_points}"
        else:  
            total = place_points + meters_points

        return total
     

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))

