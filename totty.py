import telegram.ext as tele
import telegram
import logging 

logging.basicConfig(level=logging.INFO)

TOKEN = '7887542328:AAFIPwqwF6BC5YzDMsONND6lBwZaic9mfN8'

admins=[]
owner = 5816482345

def mains():
    updater = tele.Updater(TOKEN, update_queue=None)
    # ... rest of the code ...
    def start(update, context):
        context.bot.send_photo(chat_id=(update_effective_chat_id), photo=open('photo_2024-11-12_13-46-07.jpg', 'rb'), caption='''WELCOME TO HEXA ALL IN ONE  AUCTION
                           
                           YOU CAN SEND THE POKEMONS,TMS,TEAMS,SHINES TO OUR AUCTION
                                JUST USE /append COMMAND TO ADD THE ITEMS IN OUR AUCTION''')
    
    def help(update, context):
        context.bot.send_photo(chat_id=(update_effective_chat_id), photo=open('photo_2024-11-12_13-46-07.jpg','rb'), caption='just contact us in our main group ')
    
    def advance(update, context):
        if (update_effective_user_id) == owner:
            user_id = int(context.args[0])
            admins.append(user_id)
            context.bot.send_message(chat_id=(update_effective_chat_id), text=f'User {user_id} promoted!')
        else:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Only admins can promote users!')
        
    def append(update, context):
        if update.effective_chat.type == 'private':
            context.bot.send_message(chat_id=(update_effective_chat_id), text='What do you want to add?')
            keyboard = [
                [InlineKeyboardButton('6L', callback_data='6L')],
                [InlineKeyboardButton('0L', callback_data='0L')],
                [InlineKeyboardButton('TMS', callback_data='TMS')],
                [InlineKeyboardButton('Shiny', callback_data='Shiny')],
                [InlineKeyboardButton('Teams', callback_data='Teams')],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Choose an option:', reply_markup=reply_markup)
        else:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='This command only works in private chat.')
        
    def button_click(update, context):
        query = update.callback_query
        query.answer()
        if query.data in ['6L', '0L', 'Shiny']:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='What is the Pokémon name?')
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Please forward the info page.', reply_markup=ForceReply())
        
    def handle_forwarded_message(update, context):
        if update.message.forward_from:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Please forward the IVs/EVs page.', reply_markup=ForceReply())
        else:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Invalid message. Please forward the info page again.')
        
    def handle_ivs_ev_page(update, context):
        if update.message.forward_from:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Please forward the moveset page.', reply_markup=ForceReply())
        else:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Invalid message. Please forward the IVs/EVs page again.')
        
    def handle_moveset_page(update, context):
        if update.message.forward_from:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Is the Pokémon boosted?')
            keyboard = [
                [InlineKeyboardButton('Yes', callback_data='boosted')],
                [InlineKeyboardButton('No', callback_data='not_boosted')],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Choose an option:', reply_markup=reply_markup)
        else:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Invalid message. Please forward the moveset page again.')
        
    def handle_boosted(update, context):
        query = update.callback_query
        query.answer()
        if query.data == 'boosted':
            context.bot.send_message(chat_id=(update_effective_chat_id), text='What is the base price? (e.g., 100 or 100k)')
        elif query.data == 'not_boosted':
            context.bot.send_message(chat_id=(update_effective_chat_id), text='What is the base price? (e.g., 100 or 100k)')
        
    def handle_base_price(update, context):
        price = update.message.text
        context.bot.send_message(chat_id=-1002383992799, text=f'New item added by {(update_effective_user.username)} ({(update_effective_user_id)}):\n\nPrice: {price}\n\nPlease approve or disapprove.', reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('Approve', callback_data='approve')],
            [InlineKeyboardButton('Disapprove', callback_data='disapprove')],
        ]))
    
    def handle_approval(update, context):
        query = update.callback_query
        query.answer()
        if query.data == 'approve':
            context.bot.send_message(chat_id=-1002150248090, text='Item approved!')
        elif query.data == 'disapprove':
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Please provide a reason for disapproval.')

    def handle_disapproval_reason(update, context):
        reason = update.message.text
        context.bot.send_message(chat_id=(update_effective_chat_id), text=f'Disapproval reason: {reason}')
    
    def handle_message(update, context):
        if update.message.text == '.' and (update_effective_user_id) in admins:
            msg = context.bot.send_message(chat_id=(update_effective_chat_id), text='🔸')
            context.bot.edit_message_text(chat_id=(update_effective_chat_id), message_id=msg.message_id, text='🔸🔹')
            context.bot.edit_message_text(chat_id=(update_effective_chat_id), message_id=msg.message_id, text='🔸🔹🔸')
            keyboard = [
                [InlineKeyboardButton('Confirm', callback_data='confirm')],
                [InlineKeyboardButton('CANCEL', callback_data='CANCEL')],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.edit_message_text(chat_id=(update_effective_chat_id), message_id=msg.message_id, text='Wanna sell?', reply_markup=reply_markup)
        
    def handle_bid(update, context):
        if update.message.text.startswith('/bid'):
            amount = update.message.text.split(' ')[1]
            context.bot.send_message(chat_id=(update_effective_chat_id), text=f'New bid: {update.effective_user.username} ({update.effective_user.first_name}) - {amount}')

    def button_click(update, context):
        query = update.callback_query
        query.answer()
        if query.data == 'confirm' and (update_effective_user_id) in admins:
            query.edit_message_text(text='Confirmed!')

    def unsold(update, context):
        if update.message.text == '/unsold' and (update_effective_user_id) in admins:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Unsold')
        
    import json

# Load the approved data from the JSON file
    def load_approved_data():
        with open('approved_data.json', 'r') as f:
            return json.load(f)

# Save the approved data to the JSON file
    def save_approved_data(data):
        with open('approved_data.json', 'w') as f:
            json.dump(data, f)

# Get the approved items from storage
    def get_approved_items():
        data = load_approved_data()
        return data['approved_items']

# Delete the approved items from storage
    def delete_approved_items():
        data = load_approved_data()
        data['approved_items'] = []
        save_approved_data(data)

# Go command function
    def go_command(update, context):
        if (update_effective_user_id) in admins:
            approved_items = get_approved_items()
            for item in approved_items:
                context.bot.send_message(chat_id=(update_effective_chat_id), text=item['details'])
            delete_approved_items()
        else:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='You are not authorized to use this command.')

    def tag_all(update, context):
        if (update_effective_chat_id) in ADMIN_IDS:
            chat_id = (update_effective_chat_id)
            members = context.bot.get_chat_members(chat_id)
            mention = ''
            for member in members:
                mention += f'[{member.user.first_name}](tg://user?id={(update_effective_user_id)}) '
            context.bot.send_message(chat_id=chat_id, text=mention, parse_mode='Markdown')
        else:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='You are not authorized to use this command.')
        
    def broadcast(update, context):
        if (update_effective_user_id) in admins:
            message = update.message.text.split(' ', 1)[1]
            for user_id in context.bot_data['users']:
                try:
                    context.bot.send_message(chat_id=user_id, text=message)
                except Exception as e:
                    print(f'Error broadcasting to user {user_id}: {e}')
        else:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='You are not authorized to use this command.')
        
    def cancel_command(update, context):
        if (update_effective_user_id) in context.user_data:
            del context.user_data[(update_effective_user_id)]
            context.bot.send_message(chat_id=(update_effective_chat_id), text='Submission process cancelled.')
        else:
            context.bot.send_message(chat_id=(update_effective_chat_id), text='No submission process to cancel.')

    def main():

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_handler(CommandHandler('append', add_command))
        dispatcher.add_handler(CommandHandler('abandon', cancel_command))
        dispatcher.add_handler(CommandHandler('circulate', broadcast))
        dispatcher.add_handler(CommandHandler('ktag', tag_all))
        dispatcher.add_handler(CommandHandler('go', go_command))
        dispatcher.add_handler(CommandHandler('cancel', lambda update, context: cancel_command(update, context)))
        dispatcher.add_handler(CallbackQueryHandler(button_click))
        dispatcher.add_handler(MessageHandler(Filters.forwarded & Filters.text, handle_forwarded_message))
        dispatcher.add_handler(MessageHandler(Filters.forwarded & Filters.text, handle_ivs_ev_page))
        dispatcher.add_handler(MessageHandler(Filters.forwarded & Filters.text, handle_moveset_page))
        dispatcher.add_handler(MessageHandler(Filters.text, handle_base_price))
        dispatcher.add_handler(CallbackQueryHandler(handle_approval))
        dispatcher.add_handler(MessageHandler(Filters.text, handle_disapproval_reason))

        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
    mains()