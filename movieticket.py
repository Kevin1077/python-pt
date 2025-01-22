
import datetime

while True:
    print('Welcome to the Movie Ticket Booking System')

  
    print('Select a movie:')
    print('1) Interstellar')
    print('2) Inception')
    print('3) The Dark Knight')
    print('4) The Prestige')
    print('5) Dunkirk')
    movie_choice = int(input('Enter your choice (1-5): '))
    
    if movie_choice == 1:
        movie_name = 'Interstellar'
    elif movie_choice == 2:
        movie_name = 'Inception'
    elif movie_choice == 3:
        movie_name = 'The Dark Knight'
    elif movie_choice == 4:
        movie_name = 'The Prestige'
    elif movie_choice == 5:
        movie_name = 'Dunkirk'
    else:
        print('Invalid movie selection. Please try again.')
        continue

   
    ticket_count = int(input("Enter the number of tickets you want to book: "))

 
    print('Select ticket type:')
    print('1) Platinum (₹200)')
    print('2) Normal (₹100)')
    ticket_type = int(input('Enter your choice (1 or 2): '))
    
    if ticket_type == 1:
        price_per_ticket = 200
    elif ticket_type == 2:
        price_per_ticket = 100
    else:
        print('Invalid ticket type. Please try again.')
        continue

   
    print('Select show time:')
    print('1) 10:00am')
    print('2) 2:00pm')
    print('3) 6:00pm')
    print('4) 10:00pm')
    show_time_choice = int(input('Enter your choice (1-4): '))
    
    if show_time_choice == 1:
        show_time = '10:00am'
    elif show_time_choice == 2:
        show_time = '2:00pm'
    elif show_time_choice == 3:
        show_time = '6:00pm'
    elif show_time_choice == 4:
        show_time = '10:00pm'
    else:
        print('Invalid time selection. Please try again.')
        continue

  
    date_str = input('Enter the date of the show (YYYY-MM-DD): ')
    
    try:
        show_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        continue

    total_price = ticket_count * price_per_ticket
    if ticket_count > 5:
        total_price *= 0.9

    print('\nYOU HAVE SUCCESSFULLY BOOKED YOUR TICKET\nBooking Details:')
    print(f'Movie: {movie_name}')
    print(f'Tickets: {ticket_count}')
    print(f'Ticket Type: {"Platinum" if ticket_type == 1 else "Normal"}')
    print(f'Show Time: {show_time}')
    print(f'Show Date: {show_date.strftime("%Y-%m-%d")}')
    print(f'Total Price: ₹{total_price:.2f}')
    
    break
