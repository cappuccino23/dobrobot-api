from app import db


class payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    outer_id = db.Column(db.Integer, index=True)
    status = db.Column(db.String(15))
    stamp_date = db.Column(db.timestamp)
    stamp = db.Column(db.timestamp)
    description = db.Column(db.text)

    def __repr__(self):
        return '<payments {}>'.format(self.id)


class charitable_foundation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_foundation = db.Column(db.jsonb)
    stamp = db.Column(db.timestamp)

    def __repr__(self):
        return '<charitable_foundation {}>'.format(self.id)


class logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.jsonb)
    message = db.Column(db.timestamp)
    stamp = db.Column(db.timestamp)
    pay_url = db.Column(db.timestamp)
    success_callback_url = db.Column(db.timestamp)
    fail_callback_url = db.Column(db.timestamp)
    success_redirect_url = db.Column(db.timestamp)
    fail_redirect_url = db.Column(db.timestamp)

    def __repr__(self):
        return '<payments {}>'.format(self.id)