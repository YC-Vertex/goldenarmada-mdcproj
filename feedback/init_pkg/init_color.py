import colorsys
from PIL import Image
import optparse
import webcolors

### quotes:
# https://www.jb51.net/article/48875.htm
# https://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green-with-python
# https://www.hangge.com/blog/cache/detail_981.html

def color_to_color(name):
    '''
    :param name: 字符串，css3标准中的一种颜色名称，全小写、无空格
    :return: 颜色标签，0~9（红0，粉1，黄橙2，紫3，绿4，蓝5，棕6，白7，灰8，黑9），出错则返回-1
    '''
    redlist = ['indianred','lightcoral','salmon','darksalmon','lightsalmon','crimson','red','firebrick','darkred']
    pinklist = ['pink','lightpink','hotpink','deeppink','mediumvioletred','palevioletered']
    yellowlist = ['coral','tomato','orangered','darkorange','orange',\
        'gold','yellow','lightyellow','lemonchiffon','lightgodenrodyellow','papayawhip','moccasin','peachpuff','palegoldenrod','khaki','darkkhaki']
    purplelist = ['lavender','thistle','plum','violet','orchid','fuchsia','magenta','mediumorchid','mediumpurple','amethyst','blueviolet','darkviolet','darkorchid','darkmagenta','purple','indigo','slateblue','dakrslateblue','mediumslateblue']
    greenlist = ['greenyellow','chartreuse','lawngreen','lime','limegreen','palegreen','lightgreen','mediumspringgreen','springgreen','mediumseagreen','seagreen','forestgreen','green','darkgreen','yellowgreen','olivedrab','olive','darkolivegreen','mediumaquamarine','darkseagreen','lightseagreen','darkcyan','teal']
    bluelist = ['aqua','cyan','lightcyan','paleturquoise','aquamarine','turquoise','mediumturquoise','darkturquoise','cabetblue','steelblue','lightsteelblue','powderblue','lightblue','skyblue','lightskyblue','deepskyblue','dodgerblue','cornflowerblue','mediumslateblue','royalblue','blue','mediumblue','darkblue','navy','midnightblue']
    brownlist = ['cornsilk','blanchedalmond','bisque','navajowhite','wheat','burlywood','tan','rosybrown','sandybrown','goldenrod','darkgoldenrod','peru','chocolate','saddlebrown','sienna','brown','maroon']
    whitelist = ['white','lightgray','snow','honeydew','mintcream','azure','aliceblue','ghostwhite','whitesmoke','seashell','beige','oldlace','floralwhite','ivory','antiquewhite','linen','lavenderblush','mistyrose']
    graylist = ['gainsboro','silver','darkgray','gray','dimgray','lightslategray','slategray','darkslategray']
    blacklist = ['black']
    if name in redlist:
        return 0
    if name in pinklist:
        return 1
    if name in yellowlist:
        return 2
    if name in purplelist:
        return 3
    if name in greenlist:
        return 4
    if name in bluelist:
        return 5
    if name in brownlist:
        return 6
    if name in whitelist:
        return 7
    if name in graylist:
        return 8
    if name in blacklist:
        return 9
    else:
        return -1

def closest_colour(requested_colour):
    '''
    :param requested_colour: 图片的一个最主色，为rgb三色值的tuple
    :return: 字符串，css3标准中的一个颜色名

    本函数辅助"get_colour_name"函数，不单独使用。
    '''
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    '''
    :param requested_color: 图片的一个最主色，为rgb三色值的tuple
    :return: 字符串，css3标准中的一个颜色名
    '''
    try:
        actual_name = webcolors.rgb_to_name(requested_colour)
        return actual_name
    except:
        closest_name = closest_colour(requested_colour)
        return closest_name

def get_dominant_color(image):
    '''
    :param image: 通过Image.open方式获得的图片文件
    :return: 图片的主色，rgb三色值的tuple
    '''
    image = image.convert('RGBA')
    image.thumbnail((200, 200))
    max_score = 1
    dominant_color = None
    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        if a == 0:
            continue
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        y = (y - 16.0) / (235 - 16)
        if y > 0.9:
            continue
        score = (saturation + 0.1) * count
        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)
    return dominant_color

def color(img_path):
    """
    :lib: feedback
    :func: color
    :param: img_path
    :return: color_name (color tag)

    Return the color tag of a image, given the image path. 
    """
    try:
        # 通过PIL库的方式加载本地图片
        img = Image.open(img_path)
    except:
        print("data error: failed to open image using Image from PIL")
    else:
        try:
            # 获取图片主色
            color_value = get_dominant_color(img)
        except:
            print("func error: func'get_dominant_color' has an error")
        else:
            try:
                # 获取图片主色的详细名称
                d_name = get_colour_name(color_value)
            except:
                print("func error: func'get_colour_name' has an error")
            else:
                # 转换为正式的颜色标签
                color_name = color_to_color(d_name)
                return color_name