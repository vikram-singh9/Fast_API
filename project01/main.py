from fastapi import FastAPI 
import random

app = FastAPI()

famous_poetries = [
    "The woods are lovely, dark and deep,\nBut I have promises to keep,\nAnd miles to go before I sleep,\nAnd miles to go before I sleep. - Robert Frost, 'Stopping by Woods on a Snowy Evening'",
    "Shall I compare thee to a summer’s day?\nThou art more lovely and more temperate:\nRough winds do shake the darling buds of May,\nAnd summer’s lease hath all too short a date: - William Shakespeare, 'Sonnet 18'",
    "Because I could not stop for Death –\nHe kindly stopped for me –\nThe Carriage held but just Ourselves –\nAnd Immortality. - Emily Dickinson, 'Because I could not stop for Death'",
    "Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth; - Robert Frost, 'The Road Not Taken'",
    "O Captain! my Captain! our fearful trip is done,\nThe ship has weather’d every rack, the prize we sought is won,\nThe port is near, the bells I hear, the people all exulting, - Walt Whitman, 'O Captain! My Captain!'"
]

famous_quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "To be or not to be, that is the question. - William Shakespeare",
    "That which does not kill us makes us stronger. - Friedrich Nietzsche",
    "The best way to predict your future is to create it. - Abraham Lincoln",
    "Life is what happens when you're busy making other plans. - John Lennon"
]

@app.get("/famous_poetries")
def get_famous_poetries():
    """returing random poetries"""
    return {"Famous Poetries ": random.choice(famous_poetries)}
   
@app.get("/famous_quotes")
def get_famous_poetries():
    """returing random quotes"""
    return {"Famous quotes ": random.choice(famous_poetries)}
   
