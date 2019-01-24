global divider 

def main():
    
    html = open('index.html', 'a')
    css = open('style.css', 'a')
    
    
    available_templates = ['minimal', 'portfolio', 'modern']
    
    
    divider = '----------------------------------------------'
    print(divider)
    print('|             Website Generator              |')
    print(divider)
    
    website_name = input('Enter the name of your webpage: ')
    
    html.write(
    '''
    <!DOCTYPE html>
    <html>

    <head>

    <title>''' + website_name + ''' | Home</title>    
    <link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Roboto+Slab" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous"> 
    <link rel='stylesheet' type='text/css' href='style.css'>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    </head>
    ''')
    
    print()
    print('Below is a list of the current templates we offer. Please select one to get started:')
    
    for option in available_templates:
        print('- ' + option)
    
    print()
    
    template_choice = input('Your template choice: ').lower()
    
#    while not template_choice in available_templates:
#        print()
#        print('''Sorry, that's not an available template. Please choose from the list above.''')
#        template_choice = input('Your template choice: ').lower()
    
#    if template_choice == 'modern':
#        modern()
#    elif template_choice == 'minimal':
#        minimal()
#    else:
#        portfolio()
        

main()