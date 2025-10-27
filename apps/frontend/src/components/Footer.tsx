import { Link } from 'react-router-dom';

export function Footer() {
  return (
    <footer className="mt-auto border-t bg-card">
      <div className="container py-8">
        <div className="flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="flex items-center space-x-2">
            <img src="/logo.svg" alt="Insider" className="h-6 w-auto" />
          </div>
          <div className="flex gap-6 text-sm text-muted-foreground">
            <Link to="/privacy" className="hover:text-foreground transition-colors">
              Privacy Policy
            </Link>
            <Link to="/terms" className="hover:text-foreground transition-colors">
              Terms of Service
            </Link>
            <Link to="/data-deletion" className="hover:text-foreground transition-colors">
              Data Deletion
            </Link>
          </div>
          <p className="text-sm text-muted-foreground">
            © 2025 Insider. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
