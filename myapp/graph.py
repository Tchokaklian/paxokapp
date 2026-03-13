import matplotlib.pyplot as plt
import base64
from io import BytesIO
import heapq
import matplotlib.patches as mpatches

def top_10_biggest(numbers):
    return heapq.nlargest(10, numbers)

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format= 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)   
    graph = graph.decode('utf-8')    
    buffer.close()
    return graph

def get_color_for_user(user_index):
    """Retourne une couleur unique pour chaque utilisateur"""
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan']
    return colors[user_index % len(colors)]

def get_plot_team(users_data):
    """Crée un graphique de puissances pour l'équipe avec légende
    users_data est une liste de dictionnaires: [{'user_name': 'name', 'x': [...], 'y': [...], 'n': [...]}, ...]
    """
    plt.switch_backend('AGG')    
    plt.figure(figsize=(15,8))
    plt.title('Puissances')
    
    legend_patches = []
    
    for user_index, user_data in enumerate(users_data):
        x = user_data['x']
        y = user_data['y']
        n = user_data.get('n', [])
        user_name = user_data['user_name']
        color = get_color_for_user(user_index)
        
        plt.scatter(x, y, color=color, label=user_name, s=50)
        legend_patches.append(mpatches.Patch(color=color, label=user_name))
        
        # Ajouter les annotations avec les dates
        for i, txt in enumerate(n):
            if i < len(x) and i < len(y):
                plt.annotate(str(txt), (x[i], y[i]), fontsize=8, alpha=0.7)
    
    plt.xlabel('Distance (Km)')
    plt.ylabel('Puissance (Watt)')
    plt.legend(handles=legend_patches, loc='lower left')
    plt.tight_layout()
    graph = get_graph()
    
    return graph

def get_plot(x,y,n):

    tsize=len(x)
     
    top10Km = top_10_biggest(x)
    top10Watt = top_10_biggest(y)

    plt.switch_backend('AGG')    
    plt.figure(figsize=(15,8))
    plt.title('Puissances')

    mycolor = []
    
    # Last 10 rides    
    for indice in range(len(x)):                
        if indice> tsize-10:
            mycolor.append('green')
        else:
            mycolor.append('blue')                

    plt.scatter(x, y, color= mycolor)
            
    for i, txt in enumerate(n):

        # text sur les 10 dernieres
        if i>tsize-10:
            plt.annotate(txt, (x[i], y[i]))

        # text sur les meilleures puissances 
        if y[i] >= top10Watt[9]:
            plt.annotate(txt, (x[i], y[i]))

        # text sur les plus longues        
        if x[i] >= top10Km[9]:
            plt.annotate(txt, (x[i], y[i]))            
    
    plt.xlabel('Distance (Km)')
    plt.ylabel('Puissance (Watt)') 
    plt.tight_layout()
    graph = get_graph()

    return graph