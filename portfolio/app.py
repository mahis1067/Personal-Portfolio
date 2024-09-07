from flask import Flask, render_template
from collections import deque, Counter

app = Flask(__name__)

# Use deque to maintain a fixed-size list of recent visits
last_five_visits = deque(maxlen=5)

# Define page attributes
page_attributes = {
    "hack": ["Innovation", "Teamwork", "Technical Skill", "Problem Solving", "Creativity"],
    "rob": ["Innovation", "Teamwork", "Technical Skill", "Engineering", "Learning"],
    "stem": ["Innovation", "Technical Skill", "Club", "Problem Solving", "Research"],
    "vid": ["Creativity", "Technical Skill", "Club", "Storytelling", "Visual Arts"],
    "cs50": ["Innovation", "Technical Skill", "Learning", "Problem Solving", "Coding"],
    "gall": ["Creativity", "Innovation", "Visual Arts", "Presentation", "Inspiration"],
    "ani": ["Creativity", "Technical Skill", "Learning", "Storytelling", "Visual Arts"],
    "bad/dance": ["Teamwork", "Physical Skill", "Strategy", "Coordination", "Discipline"],
    "tutor": ["Learning", "Teamwork", "Communication", "Mentoring", "Teaching"],
    "therapy": ["Teamwork", "Learning", "Empathy", "Communication", "Support"],
    "math": ["Innovation", "Technical Skill", "Learning", "Problem Solving", "Analytical Thinking"],
    "cs": ["Innovation", "Technical Skill", "Learning", "Problem Solving", "Coding"]
}

page_rec_images = {
    "hack":'static/hack_rec.jpg',
    "rob": 'static/rob_rec.jpg',
    "stem": 'static/stem_rec.jpg',
    "vid": 'static/vid_rec.jpg',
    "cs50": 'static/cs50_rec.jpg',
    "gall": 'static/gall_rec.jpg',
    "ani": 'static/ani_rec.jpg',
    "bad/dance": 'static/bad_rec.jpg',
    "tutor": 'static/tutor_rec.jpg',
    "therapy": 'static/therapy_rec.jpg',
    "math": 'static/math_rec.jpg',
    "stem": 'static/stem_rec.jpg'
}

def recent_visits(listt, page):
    listt.append(page)
    return listt

def recommend_pages(last_visits, all_pages, num_recommendations=3):
    # Extract all attributes from the last visits
    all_attributes = []
    for visit in last_visits:
        all_attributes.extend(page_attributes[visit])
    
    # Count the frequency of each attribute
    attribute_count = Counter(all_attributes)
    
    # Score pages based on the frequency of their attributes
    page_scores = {}
    for page, attributes in all_pages.items():
        score = sum(attribute_count[attr] for attr in attributes)
        page_scores[page] = score
    
    # Sort pages by score and exclude already visited pages
    recommended_pages = [page for page, score in sorted(page_scores.items(), key=lambda x: x[1], reverse=True) if page not in last_visits]
    
    # Return the top recommended pages
    return recommended_pages[:num_recommendations]

@app.route('/')
def home():
    recommendations = recommend_pages(last_five_visits, page_attributes)
    return render_template('main.html', recent_visits=last_five_visits, recommendations=recommendations)


@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/tech/hackathons')
def hack():
    recent_visits(last_five_visits, "hack")
    return render_template('tech/hackathons.html')

@app.route('/tech/robotics')
def rob():
    recent_visits(last_five_visits, "rob")
    return render_template('tech/robotics.html')

@app.route('/tech/stem')
def stem():
    recent_visits(last_five_visits, "stem")
    return render_template('tech/stem.html')

@app.route('/tech/video')
def vid():
    recent_visits(last_five_visits, "vid")
    return render_template('tech/video.html')

@app.route('/tech/cs50')
def cs50():
    recent_visits(last_five_visits, "cs50")
    return render_template('tech/cs50.html')

@app.route('/art')
def art():
    return render_template('art.html')

@app.route('/art/gallery')
def gall():
    recent_visits(last_five_visits, "gall")
    return render_template('art/gallery.html')

@app.route('/art/animation')
def ani():
    recent_visits(last_five_visits, "ani")
    return render_template('art/animation.html')

@app.route('/sd')
def sports_dance():
    return render_template('sports_dance.html')

@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')

@app.route('/volunteer/tutor')
def tutor():
    recent_visits(last_five_visits, "tutor")
    return render_template('volunteer/tutor.html')

@app.route('/volunteer/therapy')
def therapy():
    recent_visits(last_five_visits, "therapy")
    return render_template('volunteer/therapy.html')

@app.route('/wloo_comp')
def wloo_comp():
    return render_template('wloo_comp.html')

@app.route('/wloo_comp/math')
def math():
    recent_visits(last_five_visits, "math")
    return render_template('wloo_comp/math.html')

@app.route('/wloo_comp/cs')
def cs():
    recent_visits(last_five_visits, "cs")
    return render_template('wloo_comp/cs.html')

if __name__ == '__main__':
    app.run(debug=True)
