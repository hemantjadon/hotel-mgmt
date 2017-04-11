from django import forms
from .models import Booking
from room.models import Room
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

    def clean(self, *args, **kwargs):
        cleaned_data = super(BookingForm,self).clean(*args, **kwargs)

        try:
            s2 = check_in_date = cleaned_data['check_in_date']
            e2 = check_out_date = cleaned_data['check_out_date']
            room = cleaned_data['room']
        except KeyError:
            raise ValidationError('')

        bookings = room.bookings.all()

        todayDate = date.today()

        if ((check_out_date <= check_in_date) or (check_in_date < todayDate)):
            raise ValidationError(
               _('Check-In date should not be after Check-Out date and Booking can only be done in future date.')
            )
        
        if (check_in_date > (todayDate.replace(todayDate.year + 1, todayDate.month, todayDate.day))):
            raise ValidationError(
               _('Cannot book for beyond 1 year.')
            )
        
        if ((check_out_date-check_in_date).days > 30):
            raise ValidationError(
               _('Cannot stay for too long')
            )

        if (len(bookings) > 0):
            for booking in bookings:
                s1 = booking.check_in_date
                e1 = booking.check_out_date

                if (s2 >= s1 and s2 <= e1):
                    pass

                elif (e2 <= e1 and e2 >= s1):
                    pass

                elif (s2 <= s1 and e1 <= e2):
                    pass
                    
                else:
                    return cleaned_data
        else:
            return cleaned_data
        
        booked = list()
        available = list()
        
        rooms = Room.objects.all()

        for room in rooms:
            bookings = room.bookings.all()
            
            if (len(bookings) > 0):
                for booking in bookings:
                    s1 = booking.check_in_date
                    e1 = booking.check_out_date

                    if (s2 >= s1 and s2 <= e1):
                        booked.append(room)

                    elif (e2 <= e1 and e2 >= s1):
                        booked.append(room)                    
                        
                    elif (s2 <= s1 and e1 <= e2):
                        booked.append(room)                                      
                        
                    else:
                        available.append(room)
            else:
                available.append(room)
                    
        print (booked)
        print (available)
        
        if (len(available) == 0):
            raise ValidationError(
                _('Sorry, No Rooms are available during this period.')
            )
        else:
            s = 'Sorry, This room is not available during this period. Only ' + str(len(available)) + ' rooms are vacant: '

            for room in available:
                s = s + str(room.room_no) + ', '
            
            raise ValidationError(s)

        return cleaned_data
