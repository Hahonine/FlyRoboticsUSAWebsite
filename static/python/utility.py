navbar_list = [
    {
        "liclass": "sidebar-menu__item active",
        "class": "fa-home dark-bg unified-text",
        "href": "index",
        "text": ""
    },

    {
        "liclass": "sidebar-menu__item",
        "class": "fa-info-circle dark-bg unified-text",
        "href": "contact",
        "text": ""
    }
]

def getActive(menu_list, item_active, item_str, active_str):
    menu_dict = []

    for i in range(0,len(menu_list)):
        item = menu_list[i]
        if i == item_active-1:
            item["liclass"] = active_str
        else:
            item["liclass"] = item_str
        menu_dict.append(item)
    return menu_dict
