class AuthRouter:
    route_app_labels={'user','admin','contenttypes','sessions'}

    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users'
        return None

    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users'
        return None