divider = '----------------------------------------------'

def main():
    
    html = open('index.html', 'a')
    css = open('style.css', 'a')
    
    
    available_templates = {'minimal':'A simple website with apre-set color shceme with clean, minimal colors.',
                           'portfolio':'''A website to show off any projects you've made. Contains everything in the minal setup with an additional section to show off projects.''',
                           }
    
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
    print('TIP: type "info templatename" to learn more about that type of website.\n')
    
    for option in available_templates:
        print('- ' + option.capitalize())
    
    print()
    
    check = False
    
    while check != True:
        template_choice = input('Your template choice: ').lower()
        user_choice = template_choice.split(' ')
        
        if user_choice[0] == 'info':
            try:
                print()
                print(available_templates[user_choice[1]] + '\n')
            except KeyError:
                print()
                print('''Sorry, that's not an available template. Please choose from the list above.''')
                template_choice = input('Your template choice: ').lower()
        
        else:
            while not template_choice in available_templates:
                print()
                print('''Sorry, that's not an available template. Please choose from the list above.''')
                template_choice = input('Your template choice: ').lower()
            
            if template_choice == 'modern':
                modern(html, css, website_name)
                check = True
            elif template_choice == 'minimal':
                minimal(html, css, website_name)
                check = True
            elif template_choice == 'custom':
                custom(html, css, website_name)
                check = True


def minimal(html, css, website_name):
    print(divider)
    print('|                  Minimal                   |')
    print(divider)
    print()
    html.write(
    '''
<body class='bg-light'>

    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top " id='main-nav'>
  
    '''
    )
    
    
    logo = input('Does your website have a logo (Yes/No)? ').lower()
    
    if logo == 'yes':
        logo_url = input('Okay, please provide the url to your logo: ')
        html.write(
        '''<a class="navbar-brand"><img src="''' + logo_url +'''"></a> '''
        )
    if logo == 'no':
        print('''No problem! We will use your website's name as the logo.''')
        html.write(
        '''<a class="navbar-brand" href="index.html">''' + website_name + '''</a>'''
        )
    
    html.write(
    '''
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

        <div class='container'>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ml-auto">
            
    '''
    )
    
    section_amount = int(input('How many sections will you have in your website? '))
    
    while not sections.isnumeric():
        sections = int(input('How many sections will you have in your website? '))
    
    sections = []
    
    for i in range(0,sections):
        section = input('Name of section', i + ': ')
        sections.append(section)
        html.write(
        '''
        <li class="nav-item">
        <a class="nav-link" href="''' + section +'''">''' + section.capitalize() + '''</a>
      </li>
        '''
        )

main()